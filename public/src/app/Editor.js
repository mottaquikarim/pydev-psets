import React, { useContext, useRef, useState } from 'react';
import "./Editor.css"
import "./Loader.css"
import "./Terminal-bar.css"

import brace from 'brace';
import AceEditor from 'react-ace';

import 'brace/mode/python';
import 'brace/theme/monokai';

import {StateContext} from './context';

const NoFile = props => {
    return <div className="no-file">
        <div className="no-file__msg">
           <div className="no-file-header">
            🎉🎊 Hello, Wrold! 🎊🎉 
           </div>
           <br/>
           Welcome! This UI allows you to run python code on your machine from within the browser environment. This obviates the need to rely heavily on terminal to run your practice problems and focus <strong>only</strong> on problem solving.
           
           <br/>
           <br/>
           <div className="no-file-footer">
            Happy coding! 🙌 🎈🙏
           </div>
        </div>
    </div>
}

const Loading = props => {
    return <div className="no-file">
        <div className="loader">
            <div className="emoji hat"></div>
            <div className="emoji confetti"></div>
            <div className="emoji balloon"></div>
            <div className="emoji hands"></div>
        </div> 
    </div>
}

const Terminal = props => {
    const {state, dispatch} = useContext(StateContext)
    const {currentFile,} = state;

    const iframeEl = useRef(null);
    const iframe = iframeEl.current;
    if (iframe) {
        const doc = iframe.contentDocument;
        doc.body.style.color = 'white';
        doc.body.style.fontFamily = 'Roboto Mono';
        doc.body.innerHTML = currentFile.testContent;
    }

    return <div className="terminal">
        <iframe ref={iframeEl} style={{
            border: 'none',
            width: '100%',
            height: '100%',
        }}/>
    </div>
}

const Editor = props => {
    const {state, dispatch} = useContext(StateContext)
    const {currentFile,} = state;
    const [l, setL] = useState(false)
    const [c, setC] = useState('')

    if (!Object.keys(currentFile).length) {
        return <NoFile />
    }

    if (!currentFile.content) {
        return <Loading />
    }

    console.log('C is', c)
    if (!c) setC(currentFile.content)

    if (!currentFile.testContent) {
        fetch('http://localhost:5000/pyversion')
            .then(resp => resp.json())
            .then(data => dispatch({
                type: 'UPDATE_CURRENT_FILE_CONTENT',
                payload: Object.assign({}, currentFile, {
                    testContent: data.content,
                }),
            }))
     }

    let timeout = null;
    const url = 'http://localhost:5000/path/' + currentFile.filename;
    const onChange = e => {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            setL(true)
            fetch(url, {
                method: "POST",            
                mode: "cors",
                cache: "no-cache",
                credentials: "same-origin",
                headers: {
                    "Content-Type": "application/json",
                }, 
                body: JSON.stringify({"content": e}),
            })
            .then(d => {
                setC(e)
                setL(false)
            })
        }, 750);
    }

    const run = e => {
        if (l) {console.log('nope'); return;}
        const tUrl = 'http://localhost:5000/test/' + currentFile.filename;
        fetch(tUrl, {
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            credentials: "same-origin",
            headers: {
                "Content-Type": "application/json",
            }, 
            body: JSON.stringify({}),
        })
        .then(response => response.json())
        .then(data => dispatch({
            type: 'UPDATE_CURRENT_FILE_CONTENT',
            payload: Object.assign({}, currentFile, {
                testContent: data.content,
            }),
        }))
    }

    const exec = e => {

        const rUrl = 'http://localhost:5000/run/' + currentFile.filename;
        fetch(rUrl, {
            method: "POST",
            mode: "cors",
            cache: "no-cache",
            credentials: "same-origin",
            headers: {
                "Content-Type": "application/json",
            }, 
            body: JSON.stringify({}),
        })
        .then(response => response.json())
        .then(data => dispatch({
            type: 'UPDATE_CURRENT_FILE_CONTENT',
            payload: Object.assign({}, currentFile, {
                testContent: data.content,
            }),
        }))
    }

    return <div className="editor">
        <div className="terminal-bar">
            <div className="terminal-bar-header">
                {currentFile.docstring}
            </div>
            <div className={"terminal-bar-buttons " + (l ? "terminal-bar-buttons--inactive" : "")}>
                <div className="terminal-bar-run" onClick={exec}>
                   Run
                </div>
                <div className="terminal-bar-test" onClick={run}>
                   Test
                </div>
            </div>
        </div>
        <AceEditor
          placeholder="Placeholder Text"
          mode="python"
          theme="monokai"
          name="blah2"
          fontSize={14}
          showPrintMargin={true}
          showGutter={true}
          highlightActiveLine={true}
          value={c}
          onChange={onChange}
          setOptions={{
              enableBasicAutocompletion: false,
              enableLiveAutocompletion: false,
              enableSnippets: false,
              showLineNumbers: true,
              tabSize: 2,
              wrap: true,
              useWrapMode: true,
          }}/>
        <Terminal />
    </div>
}

export default Editor;
