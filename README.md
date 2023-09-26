
# dispatchx

## Overview

View more on the wiki.

--> **Happy Bug Fixing Week! (last week of every month)**



(p.s i am now committing with messages that are actually kind of useful. if you want to join me then please do)

*Please note that this project is very much a work in progress. Tread with caution.*

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
