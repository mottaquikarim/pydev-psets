import React from 'react';
import './App.css';
import Storage from "./storage";
import {
    request,
    getPath,
} from "./github";

class App extends React.Component {
    stateModes = [0, 1];
    statePtr = 0;

    constructor(props) {
        super(props);

        this.storage = new Storage();
        const stateModes = this.storage.getStateModes(); 
        this.statePtr = stateModes.length;

        this.state = {
            stateMode: this.stateModes[this.statePtr],
            githubTokenVal: '',
        }


        for (const stateMode of this.stateModes) {
            this[`renderState${stateMode}`] = this[`renderState${stateMode}`].bind(this)
        }
    }

    componentDidMount() {
        if (!this.storage.token) return;

        this.getPsets();
    }

    render() {
      const {stateMode} = this.state;
      const renderMethod = this[`renderState${stateMode}`]

      return (
        <div className="App">
          <header className="App-header">
            {renderMethod()}
          </header>
        </div>
      );
    }

    renderState0() {
        return <>
            <input 
                type="text"
                placeholder="Github Access Token" 
                className="input-field"
                value={this.state.githubTokenVal}
                onKeyDown={this.onKeyDown}
                onChange={this.onChange}/>
            <button className="input-btn" onClick={this.setToken}>Save</button>
        </>
    }

    renderState1() {
        return <>
            <p>Hello!</p>
        </>
    }

    onChange = (e) => {
        this.setState({
            githubTokenVal: e.target.value,
        })
    }

    onKeyDown = e => {
        if (e.keyCode === 13) {
            this.setToken(e);
        }
    }

    setToken = e => {
        this.storage.setItem('token', this.state.githubTokenVal)
        this.storage.setItem('stateModes', this.storage.getStateModes().concat([this.stateModes[this.statePtr]]))

        this.getPsets();

        this.setState({
            stateMode: this.stateModes[++this.statePtr],
            githubTokenVal: '',
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
            .then(all => console.log(all))
    }

}

export default App;
