import React, { useContext } from 'react';

import {StateContext} from './context';

const File = props => {
    const {state, dispatch} = useContext(StateContext)
    const {data,} = props;
    const handleClick = e => {
        e.preventDefault();
        e.stopPropagation();
        dispatch({
            type: 'UPDATE_CURRENT_FILE',
            payload: data,
        })

        const url = 'http://localhost:5000/path/' + data.filename;
        fetch(url)
            .then(resp => resp.json())
            .then(fileContent => {
                dispatch({
                    type: 'UPDATE_CURRENT_FILE_CONTENT',
                    payload: Object.assign({}, data, {
                        content: fileContent.content, 
                    }),
                })
            })
            .then(() => {
                props.history.push('/path/'+data.filename)
            })
    }

    const _props = {
        'className': "file",
        'onClick': handleClick,
    }
    const classNames = []
    if (state.currentFile.filename === data.filename || props.location.pathname.indexOf(data.filename) > -1) {
        classNames.push('active')
    }
    return <li {..._props}>
        <a href={"#/path/"+data.filename} className={classNames.join(" ")}>
            {data.docstring}
        </a>
    </li>
}

export default File;
