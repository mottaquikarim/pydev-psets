import React, { useState, useEffect, useRef } from 'react';
import brace from 'brace';
import AceEditor from 'react-ace';

import 'brace/mode/python';
import 'brace/theme/monokai';

import "./Editor.css";
const Terminal = props => {
    const [term, setTerm] = useState('>> Loading...')
    const iframeEl = useRef(null);
    const url = 'http://localhost:5000' + '/test/' + props.locationData.pathname.split('/').slice(2).join('/')
    if (term === ">> Loading...") {
        fetch('http://localhost:5000/pyversion')
            .then(resp => resp.json())
            .then(data => {
                const iframe = iframeEl.current;
                const doc = iframe.contentDocument;
                doc.body.style.color = 'white';
                doc.body.innerHTML = data.content;
            })
    }

    const run = e => {
        fetch(url, {
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
            const iframe = iframeEl.current;
            const doc = iframe.contentDocument;
            doc.body.style.color = 'white';
            doc.body.innerHTML = data.content;
        })
    }
    return <div className="terminal">
        <div className="terminal-bar" onClick={run}>
            Run Tests 
        </div>
        <iframe ref={iframeEl} style={{
            border: 'none',
            width: '100%',
            height: '100%',
        }}/>
   </div>
}

const Editor = props => {
    const [val, setVal] = useState('')
    const url = 'http://localhost:5000' + props.locationData.pathname

    fetch(url)
        .then(resp => resp.json())
        .then(data => {
            setVal(data.content)
        })

    let timeout = null;
    const onChange = e => {
        clearTimeout(timeout);
        timeout = setTimeout(() => {
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
        }, 2000);
    }
    return <div className="editor">
        <AceEditor
          placeholder="Placeholder Text"
          mode="python"
          theme="monokai"
          name="blah2"
          fontSize={14}
          showPrintMargin={true}
          showGutter={true}
          highlightActiveLine={true}
          value={val}
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
         <Terminal {...props} />
    </div>
}

export {Editor}
