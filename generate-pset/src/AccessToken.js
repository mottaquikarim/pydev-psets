import React from 'react';
import './App.css';

import Storage from "./storage";


export default class AccessToken extends React.Component {
    constructor(props) {
        super(props)
        this.storage = new Storage();
        this.state = {githubTokenVal: ""};
    }
    onKeyDown = e => e.keyCode === 13 ? this.setToken() : '';

    onChange = e => this.setState({
        githubTokenVal: e.target.value,
    })

    setToken = e => {
        this.storage.setItem('token', this.state.githubTokenVal)
        this.setState({
            githubTokenVal: '',
        })
        this.props.nextStateMode()
    }

    render() {
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
}


