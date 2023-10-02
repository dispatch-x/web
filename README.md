
# dispatchx

### THIS IS A NON-WORKING, SVELTEKIT VERSION OF DISPATCH.

You can visit it here: [Link](https://skit.dispatch.eu.org)

<!--**LAUNCHING ON 1/11/23**
-->

[screen sizes](https://screensizes.idea.org.uk)


## Overview

View more on the wiki.

--> **Happy Bug Fixing Week! (last week of every month)**



(p.s i am now committing with messages that are actually kind of useful. if you want to join me then please do)

(maybe not always though, i do have this precious thing called *TIME*)

<img src="https://github.com/GoneRogueProductions/dispatchx/assets/106704354/ac3146b4-a121-4fcc-a286-ef55efd074a7" alt="Girl in a jacket" width="100" height="100"> *Please note that this project is very much a work in progress. Tread with caution.*

### What is this?

#### I thought you'd already done Dispatch!

Yes, but the code was as we called it, self-obfuscating. It did not have proper distinction between backend and frontend. So `dispatchx` is round 2, where we separate the tech stack, and follow standards (eg. OpenAPI). Just a fun practice at coding, not intended to be a polished project :)

### How to use

Git clone this repository:

```shell
git clone https://github.com/GoneRogueProductions/dispatchx
```

Install packages:

```shell
npm install
```

If you want to get rid of the pesky security vulnerabilities, run this:

```shell
npx npm-force-resolutions
```

### Developer notes

In prod, you should use the `build-css` script. Only use the `build-sass-watch` script in dev.
