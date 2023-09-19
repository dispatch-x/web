!function r(s,o,a){function i(t,e){if(!o[t]){if(!s[t]){var n="function"==typeof require&&require;if(!e&&n)return n(t,!0);if(u)return u(t,!0);throw(e=new Error("Cannot find module '"+t+"'")).code="MODULE_NOT_FOUND",e}n=o[t]={exports:{}},s[t][0].call(n.exports,function(e){return i(s[t][1][e]||e)},n,n.exports,r,s,o,a)}return o[t].exports}for(var u="function"==typeof require&&require,e=0;e<a.length;e++)i(a[e]);return i}({1:[function(e,t,n){let r=document.createElement("template");r.innerHTML=`
<div class="profile">
    <slot name="image"></slot>
</div>
<div class="message-box">
    <span class="user-name"><slot name="username"></slot></span>
    <div class="message"><slot name="message"></slot></div>
</div>
            
`;class s extends HTMLElement{static get observedAttributes(){return["username"]}get username(){return this.getAttribute("username")}constructor(){super(),this.attachShadow({mode:"open"}).appendChild(r.content.cloneNode(!0))}}customElements.define("chat-box",s)},{}]},{},[1]);
//# sourceMappingURL=chat-box.js.map
