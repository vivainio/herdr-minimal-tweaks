#!/usr/bin/env python3
"""Install the herdr-minimal-tweaks layout and keys (macOS, Linux, Windows).

Copies the layout into the Herdr app home and merges keys.json into yours;
keys you already set are kept.
"""
import json
import os
import shutil
import sys
from pathlib import Path

src = Path(__file__).resolve().parent
dest = Path(os.environ.get("HERDR_APP_HOME") or Path.home() / ".config" / "herdr-app")

(dest / "layouts").mkdir(parents=True, exist_ok=True)
shutil.copy2(src / "layouts" / "herdr-minimal-tweaks.json", dest / "layouts")

keys_file = dest / "keys.json"
new = json.loads((src / "keys.json").read_text(encoding="utf-8"))
cur = json.loads(keys_file.read_text(encoding="utf-8")) if keys_file.exists() else {}
for section, keys in new.items():
    target = cur.setdefault(section, {})
    for key, action in keys.items():
        if key in target and target[key] != action:
            print(f"kept your {section} {key} = {target[key]}")
        else:
            target[key] = action
keys_file.write_text(json.dumps(cur, indent=2) + "\n", encoding="utf-8")

print(f"Installed to {dest}. Switch layout with ctrl-shift-l (cmd-shift-l on macOS).")
