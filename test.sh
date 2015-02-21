#!/bin/bash

# Clone submodules
git submodule update --init

cd docs

# Fix sphinx to ignore non-local image warnings
filename="$(find /home/travis/virtualenv/ -name environment.py)"
sed -e '/nonlocal\ image\ URI\ found/ s/^/#/' -i ${filename}

# Test documentation
OPTIONS="-n" # nit-picky mode
if [[ "$1" = "-W" ]] ; then
    OPTIONS="$OPTIONS -W"
fi
sphinx-build $OPTIONS -b html -d _build/doctrees . _build/html
