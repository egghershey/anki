# Copyright: Ankitects Pty Ltd and contributors
# License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html

import os, sys
from pathlib import Path

nonstandard_header = {
    "pip/pyqt5/install_pyqt5.py",
    "pylib/anki/importing/pauker.py",
    "pylib/anki/importing/supermemo_xml.py",
    "pylib/anki/statsbg.py",
    "pylib/tools/protoc-gen-mypy.py",
    "qt/aqt/mpv.py",
    "qt/aqt/winpaths.py",
}

if not os.path.exists("WORKSPACE"):
    print("run from workspace root")
    sys.exit(1)

found = False
for dirpath, dirnames, fnames in os.walk("."):
    dir = Path(dirpath)
    if "bazel-" in dirpath:
        continue
    if "qt/forms" in dirpath:
        continue
    for fname in fnames:
        if fname.endswith(".py"):
            path = dir / fname
            with open(path) as f:
                top = f.read(256)
                if not top.strip():
                    continue
                if str(path) in nonstandard_header:
                    continue
                if "Ankitects Pty Ltd and contributors" not in top:
                    print("missing standard copyright header:", path)
                    found = True

if found:
    sys.exit(1)