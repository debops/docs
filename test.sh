#!/bin/bash

cd docs

# Fix sphinx to ignore non-local image warnings
grep -r "nonlocal image URI found" /home/travis/*

# Test documentation
sphinx-build -nW -b html -d _build/doctrees . _build/html
