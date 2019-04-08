import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import "./Folder.css";

const recursivelyWriteTree = data => {
    if (data.docstring) return <File data={data} />

    return Object.keys(data).reduce((arr, name) => {
        console.log(name)
        if (name.indexOf('session') > -1) return arr;
        return arr.concat([<Folder name={name}>
            {recursivelyWriteTree(data[name])}
        </Folder>])
    }, [])
}

const File = props => {
    const {data,} = props;
    const handleClick = e => {
        e.stopPropagation();
    }

    const _props = {
        'className': "file",
        'onClick': handleClick,
    }
    return <li {..._props}>
        <a href={"#/path/"+data.filename}>
            {data.docstring}
        </a>
    </li>
}

const Folder = props => {
    const [isOpen, setOpened] = useState(true)
    const handleClick = e => {
        e.stopPropagation();
        setOpened(!isOpen)
    }

    const classNames = ["folder"]
    if (isOpen) {
        classNames.push("folder-open")
    }

    const name = props.name.split('.').pop()
    const _props = {
        'className': classNames.join(' '),
        'onClick': handleClick,
    }
    const children = (isOpen) ? props.children : null;
    return <li {..._props}>
        {name}
        <ul>{children}</ul>
    </li>
}

const FileTree = props => {
    const {data,} = props;
    return <div className="file-browser">
        <ul style={{paddingLeft: '0'}}>
            {recursivelyWriteTree(data)}
        </ul>
    </div>
}

export {FileTree}
