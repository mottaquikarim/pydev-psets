import React, { useState } from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';
import "./App.css"
import {Editor} from './Editor';
import {FileTree} from './FileTree';

const App = props => {
    const [data, setData] = useState({})

    if (Object.keys(data).length === 0) {
        fetch('http://localhost:5000/list/problems')
            .then(resp => resp.json())
            .then(data => setData(data))
    }

    return (
      <div>
        <FileTree data={data} />
        <HashRouter>
            <Switch>
                <Route path='/path' render={(props) => <Editor locationData={props.location} />} />
            </Switch>
        </HashRouter>
      </div>
    );
}

export default App;
