#!/bin/bash

# Clone submodules
git submodule update --init

cd docs || exit 1

make prepare

# FIXME: Remove. Deprecated by `suppress_warnings`.
# Fix sphinx to ignore non-local image warnings
filename="$(find /home/travis/virtualenv/ -name environment.py)"
sed -e '/nonlocal\ image\ URI\ found/ s/^/#/' -i "${filename}"

# Test documentation
# -n: nit-picky mode
sphinx-build -n -b html -d _build/doctrees . _build/html "$@"
