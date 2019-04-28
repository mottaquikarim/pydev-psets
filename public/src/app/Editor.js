import React, { useContext, useRef, useState } from 'react';
import useReactRouter from 'use-react-router';

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
    const { history, location, match } = useReactRouter();
    const {state, dispatch} = useContext(StateContext)
    const {currentFile,} = props;
    const iframeEl = useRef(null);
    const iframe = iframeEl.current;

    if (Object.keys(currentFile).length === 0 && iframe) {
        fetch('http://localhost:5003/pyversion')
            .then(resp => resp.json())
            .then(data => {
                const doc = iframe.contentDocument;
                doc.body.style.color = 'white';
                doc.body.style.fontFamily = 'Roboto Mono';
                doc.body.innerHTML = data.content;
            })
    }
    else if (iframe) {
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
    const { history, location, match } = useReactRouter();
    const {state, dispatch} = useContext(StateContext)
    const {currentFile,} = state;
    const terminalEl = useRef(null);
    const inputEl = useRef(null);
    const [term, setTerm] = useState({})
    const [l, setL] = useState(false)


    if (location.pathname === '/') {
        return <NoFile />
    }

    console.log(history, location)
    const url = 'http://localhost:5003' + location.pathname;
    fetch(url)
        .then(resp => resp.json())
        .then(data => {
            inputEl.current.editor.setValue(data.content, -1)
        })

    let timeout = null;
    const onChange = e => {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
            //setL(true)
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
                //setC(e)
                //setL(false)
            })
        }, 250);
    }

    const exec = (e, repl) => {
        const rUrl = url.replace('path', repl)
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
        .then(data => {
            setTerm({testContent: data.content})
        })
    }

    let fileObj = {}
    if (Object.keys(state.files).length > 0) {
        const {pathname} = location;
        const parts = pathname.split('/')
        const pathparts = parts.slice(2, -1).concat([parts.slice(2).join('.').replace('.py', '')])
        fileObj = pathparts.reduce((obj, part) => {
            obj = obj[part]; 
            return obj;
        }, {...state.files});
    }
    return <div className="editor">
        <div className="terminal-bar">
            <div className="terminal-bar-header">
                {fileObj.docstring}
            </div>
            <div className={"terminal-bar-buttons " + (l ? "terminal-bar-buttons--inactive" : "")}>
                <div className="terminal-bar-run" onClick={e => exec(e, "run")}>
                   Run
                </div>
                <div className="terminal-bar-test" onClick={e => exec(e, "test")}>
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
          onChange={onChange}
          ref={inputEl}
          setOptions={{
              enableBasicAutocompletion: false,
              enableLiveAutocompletion: false,
              enableSnippets: false,
              showLineNumbers: true,
              tabSize: 2,
              wrap: true,
              useWrapMode: true,
          }}/>
        <Terminal currentFile={term} />
    </div>
}

export default Editor;
