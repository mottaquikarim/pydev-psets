import React from 'react';
import './App.css';

import Storage from "./storage";
import AccessToken from './AccessToken';
import PSETPicker from './PSETPicker';
import Editor from './Editor';

class App extends React.Component {
    stateModes = [0, 1, 2];
    statePtr = 0;

    constructor(props) {
        super(props);

        this.storage = new Storage();
        const stateModes = this.storage.getStateModes(); 
        this.statePtr = stateModes.length;

        this.state = {
            stateMode: this.stateModes[this.statePtr],
        }

        for (const stateMode of this.stateModes) {
            this[`renderState${stateMode}`] = this[`renderState${stateMode}`].bind(this)
        }

        this.nextStateMode = this.nextStateMode.bind(this);
        this.prevStateMode = this.prevStateMode.bind(this);
    }

    nextStateMode() {
        this.storage.setItem('stateModes', this.storage.getStateModes().concat([this.stateModes[this.statePtr]]))

        this.setState({
            stateMode: this.stateModes[++this.statePtr],
        })
    }

    prevStateMode() {
        const stateModes = this.storage.getStateModes(); 
        stateModes.pop();

        this.storage.setItem('stateModes', stateModes)

        this.setState({
            stateMode: this.stateModes[--this.statePtr],
        })
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
        return <AccessToken 
            nextStateMode={this.nextStateMode}/>
    }

    renderState1() {
        return <PSETPicker
            nextStateMode={this.nextStateMode}/>
    }

    renderState2() {
        return <Editor
            nextStateMode={this.nextStateMode}
            prevStateMode={this.prevStateMode}/>
    }


}

export default App;
