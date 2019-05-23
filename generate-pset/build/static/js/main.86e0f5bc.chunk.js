(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{22:function(e,t,n){e.exports=n(55)},55:function(e,t,n){"use strict";n.r(t);var a=n(0),r=n.n(a),s=n(20),o=n.n(s),i=n(3),c=n(2),u=n(5),l=n(4),h=n(7),p=n(6),d=(n(8),function(){function e(){Object(i.a)(this,e),this.token=this.getItem("token")}return Object(c.a)(e,[{key:"getItem",value:function(e){var t=arguments.length>1&&void 0!==arguments[1]&&arguments[1],n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"[]",a=localStorage.getItem(e);return t?JSON.parse(a||n):a}},{key:"setItem",value:function(e,t){var n=t;return"string"!==typeof t&&(n=JSON.stringify(t)),localStorage.setItem(e,n),t}},{key:"removeItem",value:function(e){localStorage.removeItem(e)}}]),Object(c.a)(e,[{key:"getStateModes",value:function(){return this.getItem("stateModes",!0)}},{key:"getPset",value:function(){return this.getItem("pset",!0)}}]),e}()),m=function(e){function t(e){var n;return Object(i.a)(this,t),(n=Object(u.a)(this,Object(l.a)(t).call(this,e))).onKeyDown=function(e){return 13===e.keyCode?n.setToken():""},n.onChange=function(e){return n.setState({githubTokenVal:e.target.value})},n.setToken=function(e){n.storage.setItem("token",n.state.githubTokenVal),n.setState({githubTokenVal:""}),n.props.nextStateMode()},n.storage=new d,n.state={githubTokenVal:""},n}return Object(p.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){return r.a.createElement(r.a.Fragment,null,r.a.createElement("input",{type:"text",placeholder:"Github Access Token",className:"input-field",value:this.state.githubTokenVal,onKeyDown:this.onKeyDown,onChange:this.onChange}),r.a.createElement("button",{className:"input-btn",onClick:this.setToken},"Save"))}}]),t}(r.a.Component),f=n(9),g=n(11),v=n.n(g),y=n(21),S=n(28),b=function(e,t){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:"mottaquikarim",a=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"pydev-psets";return"/".concat(e,"/").concat(n,"/").concat(a,"/").concat(t)},k=function(e,t){var n=arguments.length>2&&void 0!==arguments[2]?arguments[2]:{},a=arguments.length>3&&void 0!==arguments[3]?arguments[3]:{},r=arguments.length>4&&void 0!==arguments[4]?arguments[4]:{},s=arguments.length>5&&void 0!==arguments[5]?arguments[5]:"https://api.github.com",o=arguments.length>6&&void 0!==arguments[6]?arguments[6]:localStorage.getItem("token");return S({url:e,baseURL:s,method:t,params:Object.assign({},n,{access_token:o}),headers:a,data:r})},O=function(e,t,n){var a=arguments.length>3&&void 0!==arguments[3]?arguments[3]:"mottaquikarim",r=arguments.length>4&&void 0!==arguments[4]?arguments[4]:"pydev-psets",s=k(b("repos","git/"+t,a,r),"GET").then(function(e){return e.data.object.sha}),o=s.then(function(e){return k(b("repos","git/commits/"+e,a,r),"GET")}).then(function(e){return e.data.sha}).then(function(t){return k(b("repos","git/trees",a,r),"POST",{},{},{base_tree:t,tree:e.map(function(e){return{mode:"100644",type:"blob",path:e.path,content:e.content}})})}).then(function(e){return e.data.sha});return Promise.all([s,o]).then(function(e){var t=Object(y.a)(e,2),s=t[0],o=t[1];return k(b("repos","git/commits",a,r),"POST",{},{},{parents:[s],tree:o,message:n})}).then(function(e){return e.data.sha}).then(function(e){return k(b("repos","git/"+t,a,r),"POST",{},{},{sha:e})}).then(function(e){var t=e.data;return console.log(t)})},E=function(e){function t(e){var n;return Object(i.a)(this,t),(n=Object(u.a)(this,Object(l.a)(t).call(this,e))).options={shouldSort:!0,threshold:.3,location:0,distance:100,maxPatternLength:32,minMatchCharLength:1,keys:["_parent","path"]},n.onChange=function(e){var t=n.fuse.search(e.target.value);n.setState({searchq:e.target.value,results:t})},n.createPset=function(e){var t=n.state.pset;n.storage.setItem("pset",t),n.props.nextStateMode()},n.storage=new d,n.state={loading:!0,searchq:"",results:[],data:[],pset:n.storage.getPset()},n.fuse=null,n}return Object(p.a)(t,e),Object(c.a)(t,[{key:"componentDidMount",value:function(){var e=this;this.getPsets().then(function(t){e.setState({loading:!1,data:t},function(){e.fuse=new v.a(t,e.options)})})}},{key:"render",value:function(){return this.state.loading?r.a.createElement("p",null,"Loading..."):r.a.createElement("div",{className:"wrapper-flex"},r.a.createElement("div",{className:"wrapper-flex-left"},r.a.createElement("div",{style:{width:"100%",display:"flex",justifyContent:"center"}},r.a.createElement("input",{type:"text",placeholder:"Search for PSET",className:"input-field",value:this.state.searchq,onChange:this.onChange})),this.renderRes()),this.renderPset())}},{key:"renderPset",value:function(){var e=this,t=this.state.pset;return 0===t.length?null:r.a.createElement("div",{className:"wrapper-flex-right"},r.a.createElement("h2",null,"Your PSET"),r.a.createElement("ol",null,t.map(function(t){return r.a.createElement("li",{key:t.sha,className:"pset-title-sub"},t._parent,"/",t.path," ",r.a.createElement("span",{onClick:function(n){return e.remove(t)}},"\u274c "))})),r.a.createElement("div",{style:{textAlign:"center"}},r.a.createElement("button",{className:"input-btn",onClick:this.createPset},"Save")))}},{key:"renderRes",value:function(){var e=this,t=this.state.results.reduce(function(e,t){var n=t._parent;return e[n]||(e[n]=[]),e[n].push(t),e},{});return r.a.createElement("ul",{className:"pset-wrap"},Object.keys(t).map(function(n){return r.a.createElement("li",{key:n},r.a.createElement("strong",{className:"pset-title"},n),r.a.createElement("ul",null,t[n].map(function(t){return r.a.createElement("li",{key:t.sha,className:"pset-title-sub",onClick:function(n){return e.choose(t)}},n,"/",t.path)})))}))}},{key:"choose",value:function(e){var t=this.state,n=t.data,a=t.searchq,r=t.pset,s=n.filter(function(t){return t.sha!==e.sha});this.fuse=new v.a(s,this.options);var o=this.fuse.search(a),i=r.concat([e]);this.setState({results:o,data:s,pset:i})}},{key:"remove",value:function(e){var t=this.state,n=t.data,a=t.searchq,r=t.pset.filter(function(t){return t.sha!==e.sha}),s=n.concat([e]);this.fuse=new v.a(s,this.options);var o=this.fuse.search(a);this.setState({pset:r,data:s,results:o})}},{key:"getPsets",value:function(){var e=this;return k(b("repos","git/refs/heads"),"GET").then(function(e){return e.data.filter(function(e){return e.ref.indexOf("master")>-1})}).then(function(t){return e.storage.setItem("masterBranch",t[0])}).then(function(e){return k(b("repos","contents/"),"GET",{ref:e.ref})}).then(function(e){return e.data.filter(function(e){return 0===e.name.indexOf("pset_")&&-1===e.name.indexOf("_ext")})}).then(function(e){return Promise.all(e.map(function(e){return k(b("repos","git/trees/"+e.sha),"GET")})).then(function(t){return t.reduce(function(t,n,a){var r={_parent:e[a].name,_parentSha:e[a].sha},s=n.data.tree.map(function(e){return Object(f.a)({},e,r)});return t.concat(s)},[])})}).then(function(e){return console.log(e),e})}}]),t}(r.a.Component),M=n(10),j=n(48);n(49),n(50);var x=function(e){function t(e){var n;return Object(i.a)(this,t),(n=Object(u.a)(this,Object(l.a)(t).call(this,e))).onChange=function(e,t){n.setState(Object(M.a)({},t,e.target.value))},n.goBack=function(e){n.props.prevStateMode()},n.save=function(e){var t=n.storage.getItem("masterBranch",!0),a=n.state,r=a.psetName,s=a.msg;s?r?O([{path:"src/PSETS/"+r,content:n.editor.getValue()}],t.ref,s,"mottaquikarim","PYTH2").then(function(e){n.setState({msg:""}),n.storage.removeItem("content"),alert("success!")}).catch(function(e){alert("fail! check console"),console.log(e)}):alert('you need to name your pset - something like "test_pset.md"'):alert("You need a commit message!")},n.storage=new d,n.state={msg:"",psetName:""},n}return Object(p.a)(t,e),Object(c.a)(t,[{key:"componentDidMount",value:function(){var e=this;this.editor=j.edit("editor");var t=this.editor;if(t.getSession().setMode("ace/mode/markdown"),t.setTheme("ace/theme/monokai"),t.getSession().setUseWrapMode(!0),t.setReadOnly(!0),t.getSession().on("change",function(){var n=t.getValue();e.storage.setItem("content",n)}),this.storage.getItem("content"))return t.getSession().setValue(this.storage.getItem("content")),void t.setReadOnly(!1);t.getSession().setValue("Loading...");var n=this.storage.getPset(),a=this.storage.getItem("masterBranch",!0),r=n.map(function(e){return k(b("repos","git/trees/"+e.sha),"GET")}),s=[];Promise.all(r).then(function(e){return e.reduce(function(e,t,a){var r=t.data.tree.filter(function(e){return e.path.indexOf(".py")>-1}).map(function(e){return Object(f.a)({},e,{_parent:n[a].path,_parentsha:n[a].sha,_gparent:n[a]._parent,_gparentsha:n[a]._parentSha})});return e.concat(r)},[])}).then(function(e){return s=e,e}).then(function(e){return Promise.all(e.map(function(e){return k(b("repos","contents/"+e._gparent+"/"+e._parent+"/"+e.path),"GET",{ref:a.ref})}))}).then(function(e){return e.reduce(function(e,t,n){var a=t.data,r=s[n];return a.content=atob(a.content),e[r._gparent]||(e[r._gparent]={}),e[r._gparent][r._parent]||(e[r._gparent][r._parent]=[]),e[r._gparent][r._parent].push(a),e},{})}).then(function(e){for(var n=[],a=0,r=Object.keys(e);a<r.length;a++){var s=r[a],o=e[s],i=s.slice(4).split("_").join(" ").toUpperCase();n.push("# ".concat(i,"\n"));for(var c=0,u=Object.keys(o);c<u.length;c++){var l=u[c];n.push("## ".concat(l.toUpperCase(),"\n"));var h=o[l],p=!0,d=!1,m=void 0;try{for(var f,g=h[Symbol.iterator]();!(p=(f=g.next()).done);p=!0){var v=f.value;n.push("### ".concat(v.name.toUpperCase(),"\n")),n.push("\n\n```python\n"+v.content+"\n```\n\n")}}catch(y){d=!0,m=y}finally{try{p||null==g.return||g.return()}finally{if(d)throw m}}}}console.log(e),t.getSession().setValue(n.join("\n")),t.setReadOnly(!1)})}},{key:"render",value:function(){var e=this;return r.a.createElement("div",{className:"wrapper-flex",style:{minHeight:"100vh"}},r.a.createElement("div",{style:{width:"15%"}},r.a.createElement("input",{type:"text",placeholder:"my_pset.md",className:"input-field-sm",value:this.state.psetName,onChange:function(t){return e.onChange(t,"psetName")}}),r.a.createElement("input",{type:"text",placeholder:"Commit message",className:"input-field-sm",value:this.state.msg,onChange:function(t){return e.onChange(t,"msg")}}),r.a.createElement("button",{className:"input-btn",onClick:this.goBack},"Back"),r.a.createElement("button",{className:"input-btn",onClick:this.save},"Save")),r.a.createElement("div",{className:"wrapper-flex-right",style:{width:"85%",padding:"0"}},r.a.createElement("div",{id:"editor",style:{width:"100%",height:"100%"}})))}}]),t}(r.a.Component),w=function(e){function t(e){var n;Object(i.a)(this,t),(n=Object(u.a)(this,Object(l.a)(t).call(this,e))).stateModes=[0,1,2],n.statePtr=0,n.storage=new d;var a=n.storage.getStateModes();n.statePtr=a.length,n.state={stateMode:n.stateModes[n.statePtr]};var r=!0,s=!1,o=void 0;try{for(var c,p=n.stateModes[Symbol.iterator]();!(r=(c=p.next()).done);r=!0){var m=c.value;n["renderState".concat(m)]=n["renderState".concat(m)].bind(Object(h.a)(n))}}catch(f){s=!0,o=f}finally{try{r||null==p.return||p.return()}finally{if(s)throw o}}return n.nextStateMode=n.nextStateMode.bind(Object(h.a)(n)),n.prevStateMode=n.prevStateMode.bind(Object(h.a)(n)),n}return Object(p.a)(t,e),Object(c.a)(t,[{key:"nextStateMode",value:function(){this.storage.setItem("stateModes",this.storage.getStateModes().concat([this.stateModes[this.statePtr]])),this.setState({stateMode:this.stateModes[++this.statePtr]})}},{key:"prevStateMode",value:function(){var e=this.storage.getStateModes();e.pop(),this.storage.setItem("stateModes",e),this.setState({stateMode:this.stateModes[--this.statePtr]})}},{key:"render",value:function(){var e=this.state.stateMode,t=this["renderState".concat(e)];return r.a.createElement("div",{className:"App"},r.a.createElement("header",{className:"App-header"},t()))}},{key:"renderState0",value:function(){return r.a.createElement(m,{nextStateMode:this.nextStateMode})}},{key:"renderState1",value:function(){return r.a.createElement(E,{nextStateMode:this.nextStateMode})}},{key:"renderState2",value:function(){return r.a.createElement(x,{nextStateMode:this.nextStateMode,prevStateMode:this.prevStateMode})}}]),t}(r.a.Component);o.a.render(r.a.createElement(w,null),document.getElementById("root"))},8:function(e,t,n){}},[[22,1,2]]]);
//# sourceMappingURL=main.86e0f5bc.chunk.js.map