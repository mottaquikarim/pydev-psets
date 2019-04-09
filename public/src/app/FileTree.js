import React, { useContext } from 'react';
import "./Folder.css";

import File from "./File"
import Folder from "./Folder"

import {StateContext} from './context';

const recursivelyWriteTree = data => {
    if (data.docstring) return <File data={data} />

    return Object.keys(data).reduce((arr, name) => {
        if (name.indexOf('session') > -1) return arr;
        return arr.concat([<Folder key={name} name={name}>
            {recursivelyWriteTree(data[name])}
        </Folder>])
    }, [])
}

const FileTree = props => {
    const {state, dispatch} = useContext(StateContext)
    if (Object.keys(state.files).length === 0) {
        fetch('http://localhost:5000/list/problems')
            .then(resp => resp.json())
            .then(data => dispatch({
                type: 'UPDATE_FILES',
                payload: data,
            }))
    }
    return <div className="file-browser">
        <ul style={{paddingLeft: '0'}}>
            {recursivelyWriteTree(state.files)}
        </ul>
    </div>
}

export {FileTree}
