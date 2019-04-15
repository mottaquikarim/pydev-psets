import React, { useContext, useState } from 'react';
import "./Folder.css";

import File from "./File"
import Folder from "./Folder"

import {StateContext} from './context';

const recursivelyWriteTree = (data, props) => {
    if (data.docstring) return <File data={data} {...props} />

    return Object.keys(data).reduce((arr, name) => {
        if (name.indexOf('session') > -1) return arr;
        return arr.concat([<Folder key={name} name={name} data={data[name]}>
            {recursivelyWriteTree(data[name], props)}
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
    const [isHiding, setIsHiding] = useState(false)

    return <div className={"file-browser " + (isHiding ? "file-browser-hidden": "")}>
        <div className="file-toggle" onClick={e => setIsHiding(!isHiding)}>
            {isHiding ? "➡️➡️":"⬅️⬅️"}
        </div>
        <ul style={{paddingLeft: '0'}}>
            {recursivelyWriteTree(state.files, props)}
        </ul>
    </div>
}

export {FileTree}
