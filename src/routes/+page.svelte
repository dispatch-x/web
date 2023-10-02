<main>
    <div class="new-f">
      <button onclick="hideF()" class="f-close"><i class="fa-solid fa-xmark"></i></button>
      <strong class="new-feature">
        New in Dispatch:
      </strong>
      <span class="new-f-desc">
        <strong>v0.1</strong> A fresh start, new interface and better code
      </span>
      <video class="new-f-demo" controlsList="nodownload" playsinline autoplay muted poster="/assets/img/templates/iphones.webp">
        <source src="/assets/img/templates/iphones.webm" type="video/webm">
      </video>
      <span class="demo-replay icon-link">
        <i class="fa-solid fa-rotate-right"></i>
        Replay
      </span>
    </div>
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
          <h1><code class="encryption mb-3 fw-semibold lh-1 text-center text-black">End to end encryption</code></h1>
          <span class="encryption-replay icon-link">
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
  

  <script>
    import Fa from 'svelte-fa'
    import { faFlag } from '@fortawesome/free-solid-svg-icons'
    import { onMount } form 'svelte';
    const jq = window.$;

    $(function() {
      $('.nav-cont').load('/modules/navbar.html');
    });

    function hideF() {
      $('.new-f').animate({
        marginTop: '-500px'
      });
      setTimeout(function(){$('.new-f').css('position','fixed');}, 200);
    }

    document.querySelector('.new-f-demo').addEventListener('ended',showReplay,false);
    function showReplay() {
      $('.demo-replay').show(200);
    }
    $('.demo-replay').on('click', function(){
      curVid = document.querySelector('.new-f-demo');
      curVid.pause();
      curVid.currentTime = '0';
      curVid.play();
    });


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

    $('.encryption-replay').on('click', replayEffect);

    const phrases = [
      'End to end encryption',
      'helps keep your data safe',
      'from hackers and spies'
    ]

    const el = document.querySelector('.encryption')
    const fx = new TextScramble(el)

    let counter = 0;
    function replayEffect() {
      
      const next = () => {
        if (el.innerText == phrases[phrases.length - 1]) {
          fx.setText(phrases[0]).then(() => {
            counter = 1;
            $('.encryption-replay').show(200);
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
    replayEffect();


  </script>