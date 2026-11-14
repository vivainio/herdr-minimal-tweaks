# Herdr Minimal Tweaks

The stock Herdr `main` window with a wider sidebar and Files/Changes panel.

## What you see
- Left sidebar, 468px, `chrome` background: `workspace-chrome` brand row (46px), `spaces` and `agents` lists, `workspace-chrome` footer (69px).
- Tab bar (`tabs`, 42px), pane cards (radius 10, gap 8, 30px headers), status bar (28px).
- Right panel (466px, hidden until toggled from the tab bar): stack `panel-body` with `files` and `changes`.

## Built from
`layouts/herdr-minimal-tweaks.json`, a clone of `main` with only the two sizes changed. Shipped mods only.

## Done when
The layout switches without `layout.error`, and the Files and Changes buttons open the panel.
