import React from 'react';
import './App.css';

import Storage from "./storage";
import {
    request,
    getPath,
    save,
} from "./github";

const ace = require('brace');
require('brace/theme/monokai');
require('brace/mode/markdown');



export default class Editor extends React.Component {
    constructor(props) {
        super(props)
        this.storage = new Storage();
        this.state = {
            msg: '',
            psetName: '',
        }
    }

    componentDidMount() {
        this.editor = ace.edit('editor');
        const editor = this.editor;

        editor.getSession().setMode('ace/mode/markdown');
        editor.setTheme('ace/theme/monokai');
        editor.getSession().setUseWrapMode(true);
        editor.setReadOnly(true); 
        editor.getSession().on('change', () => {
            const content = editor.getValue();
            this.storage.setItem('content', content)
        })
        if (this.storage.getItem('content')) {
            editor.getSession().setValue(this.storage.getItem('content'));
            editor.setReadOnly(false); 
            return;
        }
        else {
            editor.getSession().setValue('Loading...');
        }

        const pset = this.storage.getPset()
        const masterBranch = this.storage.getItem('masterBranch', true)

        const content = pset.map(curr => request(
            getPath("repos", "git/trees/" + curr.sha),
            "GET",
        ))

        let validTrees = []
        Promise
            .all(content)
            .then(items => items.reduce((arr, item, j) => {
                const {tree} = item.data;
                const validTrees = tree
                    .filter(i => i.path.indexOf('.py') > -1)
                    .map(i => ({
                        ...i, 
                        _parent: pset[j].path, 
                        _parentsha: pset[j].sha,
                        _gparent: pset[j]._parent, 
                        _gparentsha: pset[j]._parentSha,
                    }))

                return arr.concat(validTrees)
            }, []))
            .then(t => {
                validTrees = t;
                return t;
            })
            .then(all => Promise.all(all.map(curr => request(
                getPath("repos", "contents/"+curr._gparent + "/" + curr._parent + "/" + curr.path),
                "GET",
                {ref: masterBranch.ref}
            ))))
            .then(data => data.reduce((hash, {data}, i) => {
                const v = validTrees[i]
                data.content = atob(data.content);
                if (!hash[v._gparent]) hash[v._gparent] = {}
                if (!hash[v._gparent][v._parent]) hash[v._gparent][v._parent] = []

                hash[v._gparent][v._parent].push(data)
                return hash;
            }, {}))
            .then(sanitized => {
                const str = []
                for (const s of Object.keys(sanitized)) {
                    const obj = sanitized[s];
                    const header = s.slice(4).split('_').join(' ').toUpperCase()
                    str.push(`# ${header}\n`)
                    for (const t of Object.keys(obj)) {
                        str.push(`## ${t.toUpperCase()}\n`)
                        const arr = obj[t]
                        for (const a of arr) {
                            str.push(`### ${a.name.toUpperCase()}\n`)
                            str.push("\n\n```python\n" + a.content + "\n```\n\n")
                        }
                    }
                }
                console.log(sanitized)
                editor.getSession().setValue(str.join('\n'));
                editor.setReadOnly(false); 
            })

    }
    render() {
        const styles = {
            width: '100%',
            height: '100%',
        }
        return <div className="wrapper-flex" style={{
            'minHeight': '100vh',
        }}>
            <div style={{
                'width': '15%', 
            }}>
                <input 
                    type="text"
                    placeholder="my_pset.md" 
                    className="input-field-sm"
                    value={this.state.psetName}
                    onChange={e => this.onChange(e,'psetName')}/>

                <input 
                    type="text"
                    placeholder="Commit message" 
                    className="input-field-sm"
                    value={this.state.msg}
                    onChange={e => this.onChange(e,'msg')}/>

                <button className="input-btn"
                    onClick={this.goBack}>Back</button>

                <button className="input-btn"
                    onClick={this.save}>Save</button>

                <button className="input-btn"
                    onClick={this.clear}>Clear</button>
            </div>
            <div className="wrapper-flex-right" style={{
                'width': '85%',
                'padding': '0',
            }}>
                <div id="editor" style={styles}></div>
            </div>
        </div>
    }

    onChange = (e, key) => {
        this.setState({
            [key]: e.target.value,
        })
    }
    goBack = e => {
        this.props.prevStateMode();
    }
    clear = e => {
        this.storage.removeItem('content')
        alert('cleared your content, now hit the BACK button to go back and create additional PSETs')
    }

    save = e => {
        const masterBranch = this.storage.getItem('masterBranch', true)
        const {psetName, msg} = this.state;

        if (!msg) {
            alert('You need a commit message!')
            return
        }
        if (!psetName) {
            alert('you need to name your pset - something like "test_pset.md"')
            return
        }

        save([{
            "path": "src/PSETS/" + psetName,
            "content": this.editor.getValue()
        }], masterBranch.ref, msg, "mottaquikarim", "PYTH2")
        .then(data => {
            this.setState({msg: ''})
            this.storage.removeItem('content')
            alert('success!')
        })
        .catch(e => {
            alert('fail! check console')
            console.log(e)
        })
    }
}
