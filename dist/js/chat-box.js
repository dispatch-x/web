!function r(s,o,i){function a(t,e){if(!o[t]){if(!s[t]){var n="function"==typeof require&&require;if(!e&&n)return n(t,!0);if(u)return u(t,!0);throw(e=new Error("Cannot find module '"+t+"'")).code="MODULE_NOT_FOUND",e}n=o[t]={exports:{}},s[t][0].call(n.exports,function(e){return a(s[t][1][e]||e)},n,n.exports,r,s,o,i)}return o[t].exports}for(var u="function"==typeof require&&require,e=0;e<i.length;e++)a(i[e]);return a}({1:[function(e,t,n){let r=document.createElement("template");r.innerHTML=`
<div class="nl">
    <slot name="image"></slot>
</div>
<div class="nc">
    <span class="nh"><slot name="username"></slot></span>
    <div class="np"><slot name="message"></slot></div>
</div>
            
`;class s extends HTMLElement{static get observedAttributes(){return["username"]}get username(){return this.getAttribute("username")}constructor(){super(),this.attachShadow({mode:"open"}).appendChild(r.content.cloneNode(!0))}}customElements.define("chat-box",s)},{}]},{},[1]);
//# sourceMappingURL=chat-box.js.map
