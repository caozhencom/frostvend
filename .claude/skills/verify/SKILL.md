---
name: verify
description: Verify the FrostVend static website by running a local HTTP server and driving the changed page in a real browser.
---

# Website verification

Use this when a change affects the runtime behavior of the FrostVend website.

## Launch

1. Start a local static server from the repo root:
   - `python -m http.server 8001 --directory "C:/Users/阿镇/website"`
2. Confirm the page is reachable:
   - `curl -I http://127.0.0.1:8001/index.html`

## Drive in a real browser

For end-to-end verification on this machine:

1. Launch Chrome headless with DevTools:
   - `"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --disable-gpu --remote-debugging-port=9223 --user-data-dir="$(mktemp -d)" about:blank`
2. Drive the page through the DevTools Protocol from Node.
3. Capture at least one screenshot of the changed UI state.

## Flows worth driving

- Homepage hero image and product gallery changes
- 360 viewer behavior:
  - thumbnail click switches frames
  - drag switches frames
  - auto rotate advances frames rather than rotating the container
- Navigation and anchor jumps

## Gotchas

- This repo is a static site; do not verify by running tests.
- Browser cache can mask image swaps, so use versioned image URLs when needed.
- There is no project `.claude` tree by default; keep this skill minimal and runtime-focused.
