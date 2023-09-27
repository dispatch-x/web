!function r(o,s,i){function u(t,e){if(!s[t]){if(!o[t]){var n="function"==typeof require&&require;if(!e&&n)return n(t,!0);if(a)return a(t,!0);throw(e=new Error("Cannot find module '"+t+"'")).code="MODULE_NOT_FOUND",e}n=s[t]={exports:{}},o[t][0].call(n.exports,function(e){return u(o[t][1][e]||e)},n,n.exports,r,o,s,i)}return s[t].exports}for(var a="function"==typeof require&&require,e=0;e<i.length;e++)u(i[e]);return u}({1:[function(e,t,n){let r=document.createElement("template");r.innerHTML=`
<div  profile >
    <slot name="image"></slot>
</div>
<div  message-box >
    <span  user-name ><slot name="username"></slot></span>
    <div  message ><slot name="message"></slot></div>
</div>
            
`;class o extends HTMLElement{static get observedAttributes(){return["username"]}get username(){return this.getAttribute("username")}constructor(){super(),this.attachShadow({mode:"open"}).appendChild(r.content.cloneNode(!0))}}customElements.define("chat-box",o)},{}]},{},[1]);
//# sourceMappingURL=chat-box.js.map
