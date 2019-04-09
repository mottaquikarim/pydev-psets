import React, { useContext } from 'react';

import {StateContext} from './context';

const File = props => {
    const {state, dispatch} = useContext(StateContext)
    const {data,} = props;
    const handleClick = e => {
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
    }

    const _props = {
        'className': "file",
        'onClick': handleClick,
    }
    const classNames = []
    if (state.currentFile.filename === data.filename) {
        classNames.push('active')
    }
    return <li {..._props}>
        <a href={"#/path/"+data.filename} className={classNames.join(" ")}>
            {data.docstring}
        </a>
    </li>
}

export default File;
