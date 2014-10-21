#!/bin/bash

cd docs

# Fix sphinx to ignore non-local image warnings
filename="$(find /home/travis/virtualenv/ -name environment.py)"
sed -e '/nonlocal\ image\ URI\ found/ s/^/#/' -i ${filename}

# Test documentation
sphinx-build -nW -b html -d _build/doctrees . _build/html
