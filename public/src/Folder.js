import React, { useState } from 'react';
import "./Folder.css";

const Folder = props => {
    const [isOpen, setOpened] = useState(false)
    const children = (isOpen) ? props.children : null;
    const handleClick = e => {
        e.stopPropagation();
        setOpened(!isOpen)
    }

    const classNames = "folder " + ((isOpen) ? "folder-open" : "")
    const name = props.name.split('.').pop()
    return <li className={classNames} onClick={handleClick}>
        {name}
        <ul>
            {children}
        </ul>
    </li>
}

export {Folder}
