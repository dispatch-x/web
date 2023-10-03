<style lang="scss">
@import 'main';


$inset-shadow: inset 0 -1px 1px rgba(var(--bs-body-color-rgb), 0.15),0 0.25rem 1.5rem rgba(var(--bs-body-bg-rgb), 0.75);

body {
    padding: 0!important;
}


.container-sm {
    padding-top: 2em;
    font-family: 'Outfit', $font-sans-serif!important;
}

.new-f {
    background-color: #FBAB7E;
    box-shadow: $box-shadow-sm;
    background-image: linear-gradient(62deg, #FBAB7E 0%, #F7CE68 100%);
    position: sticky;
    align-items: center;
    justify-content: center;
    display: flex;
    flex-direction: column;
    padding: 1rem 0;
    .new-feature {
        width: auto;
        box-shadow: $inset-shadow;
        border-radius: 7px;
        padding: 0.3rem;
        background: $primary;
        color: white;
        font-weight: 600;
    }
    .new-f-desc {
        text-align: center;
    }
    .new-f-demo {
        box-shadow: $box-shadow-sm $inset-shadow;
        border-radius: 1rem;
        border: 1px solid $gray-500;
        margin: .5rem;
        width: 90%;
        height: auto;
    }
    .demo-replay {
        display: none;
        user-select: none;
        color: $link-color;
        cursor: pointer;
        transition: .2s;
        text-align: center;
        justify-content: center;
        align-items: center;
        &:hover {
            text-decoration: underline;
        }
    }
    .f-close {
        position: absolute;
        top: .5rem;
        right: .5rem;
        background: 0;
        border: 0;
        transform: scale(1.5);
        color: black;
        cursor: pointer;
    }
}

// h1
h1, h2, h3, h4, p, span {
    text-align: center;
}
main {
    padding-bottom: 75px;
    overflow: auto;
    text-align: center;
}
.col {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    .row {
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
}
.big-heading {
    font-size: calc(1.525rem + 3.3vw);
    text-align: center;
    width: 100%;
}
.encryption-replay {
    display: none;
    user-select: none;
    color: $link-color;
    cursor: pointer;
    transition: .2s;
    text-align: center;
    justify-content: center;
    align-items: center;
    &:hover {
        text-decoration: underline;
    }
}

</style>

<script lang="ts">
  import Navbar from "./Navbar.svelte";
  import { onMount } from 'svelte';

  let newF;
  let newFDemo;
  let demoReplay;
  let current = 0;

  onMount(() => {

  });

  function hideF() {
    current = 1;
  }

  function showReplay() {
    demoReplay.style.display = 'block';
  }
  let curVid;
  function demoClicked(){
    newFDemo.pause();
    newFDemo.currentTime = '0';
    newFDemo.play();
    
  }


  class TextScramble {
    constructor(el) {
      this.el = el
      this.chars = '!<>-_\\/[]{}—=+*^?#________'
      this.update = this.update.bind(this)
    }
    setText(newText) {
      const oldText = this.el.innerText
      const length = Math.max(oldText.length, newText.length)
      const promise = new Promise((resolve) => this.resolve = resolve)
      this.queue = []
      for (let i = 0; i < length; i++) {
        const from = oldText[i] || ''
        const to = newText[i] || ''
        const start = Math.floor(Math.random() * 40)
        const end = start + Math.floor(Math.random() * 40)
        this.queue.push({ from, to, start, end })
      }
      cancelAnimationFrame(this.frameRequest)
      this.frame = 0
      this.update()
      return promise
    }
    update() {
      let output = ''
      let complete = 0
      for (let i = 0, n = this.queue.length; i < n; i++) {
        let { from, to, start, end, char } = this.queue[i]
        if (this.frame >= end) {
          complete++
          output += to
        } else if (this.frame >= start) {
          if (!char || Math.random() < 0.28) {
            char = this.randomChar()
            this.queue[i].char = char
          }
          output += `<span class="dud">${char}</span>`
        } else {
          output += from
        }
      }
      this.el.innerHTML = output
      if (complete === this.queue.length) {
        // @ts-ignore
        this.resolve()
      } else {
        this.frameRequest = requestAnimationFrame(this.update)
        this.frame++
      }
    }
    randomChar() {
      return this.chars[Math.floor(Math.random() * this.chars.length)]
    }
  }

  
  let encryptionReplay;
  let encryption;


  const phrases = [
    'End to end encryption',
    'helps keep your data safe',
    'from hackers and spies'
  ]

  
  

  let counter = 0;
  function replayEffect() {
    const el = document.querySelector(".encryption");
    const fx = new TextScramble(el);
    const next = () => {
      if (el.innerText == phrases[phrases.length - 1]) {
        fx.setText(phrases[0]).then(() => {
          counter = 1;
          document.querySelector(".encryption-replay").style.display = 'block';
        })
      }
      else {
        fx.setText(phrases[counter]).then(() => {
          setTimeout(next, 1250)
        })
        counter = (counter + 1) % phrases.length
      }
    }
    next();
  }

  onMount(() => {
    replayEffect();
  });


</script>

<Navbar />

<div class:demoHidden="{current === 1}" class="new-f">
  <button on:click="{hideF}" class="f-close"><i class="fa-solid fa-xmark"></i></button>
  <strong class="new-feature">
    New in Dispatch:
  </strong>
  <span class="new-f-desc">
    <strong>v0.1</strong> A fresh start, new interface and better code
  </span>
  <video on:ended="{showReplay}" bind:this="{newFDemo}" class="new-f-demo" controlsList="nodownload" playsinline autoplay muted poster="/iphones.webp">
    <source src="/iphones.webm" type="video/webm">
  </video>
  <span tabindex="0" role="button" bind:this="{demoReplay}" on:click="{demoClicked}" class="demo-replay icon-link">
    <i class="fa-solid fa-rotate-right"></i>
    Replay
  </span>
</div>get r

<main style="position: relative; top: 0;">
    
    <div class="container-sm">
      <div class="col">
        <div class="row">
          <h1 class="big-heading mb-3 fw-semibold lh-1">The most <span class="h1-switch">customizable</span> chatting service out there</h1>
          <p class="lead mb-4" style="color: var(--d-secondary-color); text-align: center;">
            Whatever your style, rainbow unicorns, squared edges or the default look, express yourself with peace of mind, knowing that we do not collect any of your data.
          </p>
          <a href="/authenticate.html?state=reg" class="d-button" style="width: 100%; font-size: x-large;">Sign up now</a>
          <a target="_blank" href="https://github.com/GoneRogueProductions/dispatchx" class="d-button icon-link" style="width: 100%; background: black; border: 0; justify-content: center; margin-top: .5rem;"><i class="fa-brands fa-github"></i> View on Github</a>
        </div>
        <div class="row">
          <hr style="margin-top: 1rem;">
          <h3>Still not convinced?</h3>
          <h1><code style="font-family: var(--bs-font-monospace)!important;" class="encryption mb-3 fw-semibold lh-1 text-center text-black">End to end encryption</code></h1>
          <span tabindex="0" on:click="{replayEffect}" role="button" class="encryption-replay icon-link">
            <i class="fa-solid fa-rotate-right"></i>
            Replay
          </span>
          <p class="lead mb-4" style="color: var(--d-secondary-color); text-align: center;">
            End to end encryption is used by almost every chatting service nowadays. However, some big companies spy on your messages <em>before</em> they get encrypted, so they get looked at by someone who you don't want looking.
          </p>
          <p class="lead mb-4" style="color: var(--d-secondary-color); text-align: center;">
            However, Dispatch does not spy on your messages in any way whatsoever, and our encryption means that only the people you want seeing your messages can see them.
          </p>
        </div>
      </div>
    </div>
  </main>
  

  