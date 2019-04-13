import React from 'react';
import { Route, Switch } from 'react-router-dom';
import "../App.css"

import {StateProvider} from './context'
import {FileTree} from './FileTree';
import Editor from './Editor';


const App = props => {
    return (<div>
        <StateProvider>
            <Route path='/' component={FileTree} />
            <Switch>
                <Route path='/' exact component={Editor} />
                <Route path='/path' component={Editor} />
            </Switch>
        </StateProvider>
    </div>)
}

export default App;
