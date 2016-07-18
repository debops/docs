#!/bin/bash

# Clone submodules
git submodule update --init

cd docs || exit 1

make prepare

# Test documentation
# -n: nit-picky mode
sphinx-build -n -b html -d _build/doctrees . _build/html "$@"
