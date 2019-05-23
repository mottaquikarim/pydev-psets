import React from 'react';
import './App.css';
import Fuse from 'fuse.js';

import Storage from "./storage";
import {
    request,
    getPath,
} from "./github";


export default class PSETPicker extends React.Component {
    options = {
      shouldSort: true,
      threshold: 0.3,
      location: 0,
      distance: 100,
      maxPatternLength: 32,
      minMatchCharLength: 1,
      keys: [
        "_parent",
        "path",
        //"author.firstName"
      ]
    }

    constructor(props) {
        super(props);
        this.storage = new Storage();
        this.state = {
            loading: true,
            searchq: '',
            results: [],
            data: [],
            pset: this.storage.getPset(),
        }
        this.fuse = null;
    }

    componentDidMount() {
        this.getPsets()
            .then(data => {
                this.setState({loading: false, data}, () => {
                    this.fuse = new Fuse(data, this.options); // "list" is the item array
                })
            })
    }

    render() {
        const {loading} = this.state;

        if (loading) return <p>Loading...</p>

        return <div className="wrapper-flex">
            <div className="wrapper-flex-left">
                <div style={{
                    'width': '100%',
                    'display': 'flex',
                    'justifyContent': 'center',
                }}>
                <input 
                    type="text"
                    placeholder="Search for PSET" 
                    className="input-field"
                    value={this.state.searchq}
                    onChange={this.onChange}/>
                </div>
                {this.renderRes()}
           </div>
            {this.renderPset()}
        </div>
    }

    renderPset() {
        const {pset} = this.state;

        if (pset.length === 0) return null;

        return <div className="wrapper-flex-right">
            <h2>Your PSET</h2>
            <ol>
            {pset.map(item => {
                return <li key={item.sha} className="pset-title-sub">
                    {item._parent}/{item.path} <span onClick={e => this.remove(item)}>❌ </span>
                </li>
            })}
            </ol>
            <div style={{textAlign: 'center'}}>
                <button className="input-btn" onClick={this.createPset}>
                    Save
                </button>
            </div>
        </div>
    }

    renderRes() {
        const {results} = this.state;
        const displayable = results.reduce((hash, curr) => {
            const par = curr._parent;
            if (!hash[par]) hash[par] = [];
            hash[par].push(curr);

            return hash;
        }, {});

        return <ul className="pset-wrap">
            {Object.keys(displayable).map(key => {
                return <li key={key}>
                    <strong className="pset-title">
                        {key}
                    </strong>
                    <ul>
                    {displayable[key].map(curr => {
                        return <li key={curr.sha} className="pset-title-sub" onClick={e => this.choose(curr)}>
                            {key}/{curr.path}
                        </li>
                    })}
                    </ul>
                </li>
            })}
        </ul>
    }

    choose(curr) {
        const {data, searchq, pset} = this.state;
        const newData = data.filter(item => item.sha !== curr.sha)

        this.fuse = new Fuse(newData, this.options); // "list" is the item array
        const res = this.fuse.search(searchq)

        const newPset = pset.concat([curr])

        this.setState({
            results: res,
            data: newData,
            pset: newPset,
        })
    }

    remove(curr) {
        const {data, searchq, pset} = this.state;
        const newPset = pset.filter(p => p.sha !== curr.sha)
        const newData = data.concat([curr])

        this.fuse = new Fuse(newData, this.options); // "list" is the item array
        const res = this.fuse.search(searchq)

        this.setState({
            pset: newPset,
            data: newData,
            results: res,
        })
    }

    onChange = e => {
        const res = this.fuse.search(e.target.value)
        this.setState({
            searchq: e.target.value,
            results: res,
        })
    }

    getPsets() {
        return request(getPath("repos", "git/refs/heads"), "GET")
            // grab master branch
            .then(({data}) => data.filter(branch => branch.ref.indexOf('master') > -1))
            // store master branch info
            .then(branch => this.storage.setItem('masterBranch', branch[0]))
            // get all content from master
            .then(branch => request(getPath("repos", "contents/"), "GET", {ref: branch.ref,}))
            // drill down to only stuff that starts with "pset_"
            .then(({data}) => data.filter(item => item.name.indexOf("pset_") === 0 && item.name.indexOf("_ext") === -1))
            // get all files for pset_*
            .then(data => Promise.all(data.map(file => request(getPath("repos", "git/trees/"+file.sha), "GET",)))
                // for each file, get trees and match with parents (ie: pset_* name)
                .then(allSubFiles => allSubFiles.reduce((arr, subFile, i) => {
                    const p = {_parent: data[i].name, _parentSha: data[i].sha};
                    const children = subFile.data.tree.map(tree => ({...tree, ...p}))
                    return arr.concat(children)
                }, [])))
            // print or return, etc
            .then(all => {
                console.log(all)
                return all;
            })
    }

    createPset = e => {
        const {pset} = this.state;
        this.storage.setItem('pset', pset)
        this.props.nextStateMode()
    }
}
