import React, { useState, useEffect, useRef } from 'react';
import brace from 'brace';
import AceEditor from 'react-ace';

import 'brace/mode/python';
import 'brace/theme/monokai';

import "./Editor.css";
const Editor = props => {
    const [val, setVal] = useState('')
    let loading = false
    const url = 'http://localhost:5003' + props.locationData.pathname

    fetch(url)
        .then(resp => resp.json())
        .then(data => {
            setVal(data.content)
        })

    let timeout = null;
    const onChange = e => {
        clearTimeout(timeout);
        loading = true
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
            .then(() => loading = false)
        }, 2000);
    }

    const [term, setTerm] = useState('>> Loading...')
    const iframeEl = useRef(null);
    const tUrl = 'http://localhost:5003' + '/test/' + props.locationData.pathname.split('/').slice(2).join('/')
    if (term === ">> Loading...") {
        fetch('http://localhost:5003/pyversion')
            .then(resp => resp.json())
            .then(data => {
                const iframe = iframeEl.current;
                const doc = iframe.contentDocument;
                doc.body.style.color = 'white';
                doc.body.innerHTML = data.content;
            })
    }
    const run = e => {
        if (loading) return;

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
        .then(data => {
            const iframe = iframeEl.current;
            const doc = iframe.contentDocument;
            doc.body.style.color = 'white';
            doc.body.innerHTML = data.content;
        })
    }
    console.log('loading', loading)
    return <div className="editor">
        <div className="terminal-bar" onClick={run}>
            {loading ? "Loading...": "Run Tests"}
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
          <div className="terminal">
            <iframe ref={iframeEl} style={{
                border: 'none',
                width: '100%',
                height: '100%',
            }}/>
         </div>
    </div>
}

export {Editor}
