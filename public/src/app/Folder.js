import React, { useState } from 'react';

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

export default Folder;
