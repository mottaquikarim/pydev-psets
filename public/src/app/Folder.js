import React, { useState } from 'react';
import useReactRouter from 'use-react-router';

const isPartPath = (pathname, name) => {
    const paths = name.split('.');
    for (let path of paths) {
        if (pathname.indexOf(path) > -1) return true;
    }
    return false;
}
const Folder = props => {
    const { location } = useReactRouter();
    const openedInitState = isPartPath(location.pathname, props.name)
    const [isOpen, setOpened] = useState(openedInitState)
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
