# herdr-minimal-tweaks

A Herdr app layout: the shipped `main` layout with a wider sidebar (468px) and a wider Files/Changes panel (466px). It uses only Herdr's own mods, so it works the same on macOS, Linux and Windows. It also binds Alt+arrows: Alt+Left/Right switch tabs, Alt+Up/Down switch spaces. The installer merges these into your `keys.json` and keeps any key you already set.

## Install

`python3 install.py` (Windows: `python install.py`)

Then press `ctrl-shift-l` to cycle layouts, or run `herdr-app do layout.switch '{"name":"herdr-minimal-tweaks"}'`.

## Files and Changes buttons missing?

The tab bar shows a button for each panel listed in the per-machine setting `workspace.panels`, which a layout file can't set. If you went through the welcome screen's "Choose your panels" page without turning anything on, that list is empty and the buttons are hidden.

To fix it on a machine:

1. Open the command palette (`cmd-shift-p` on macOS, `ctrl-shift-p` on Windows/Linux) and run **Welcome** (command `app.welcome`), or run `herdr-app do app.welcome` from a terminal.
2. Go to page 3, **Choose your panels**, and turn on **Files** and **Changes**.
3. Finish or close the welcome screen. The buttons appear in the tab bar and open the panel on the right.

Skipping the welcome screen entirely leaves both panels on by default.
