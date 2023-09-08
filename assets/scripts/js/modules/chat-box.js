let tmpl = document.createElement('template');
tmpl.innerHTML = `
<div class="profile">
    <slot name="image"></slot>
</div>
<div class="message-box">
    <span class="user-name"><slot name="username"></slot></span>
    <div class="message"><slot name="message"></slot></div>
</div>
            
`

class ChatBox extends HTMLElement {

    static get observedAttributes() {
        return ['username'];
    }

    get username() {
        return this.getAttribute("username")
    }
    // Can define constructor arguments if you wish.
    constructor() {
        // If you define a constructor, always call super() first!
        // This is specific to CE and required by the spec.
        super();
  
        let shadowRoot = this.attachShadow({mode: 'open'});
        shadowRoot.appendChild(tmpl.content.cloneNode(true));
    }
  
}
  
customElements.define('chat-box', ChatBox);