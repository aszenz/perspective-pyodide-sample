#!/usr/bin/sh

set -e

# download artificat from github
VERSION=3.3.4
WHL=perspective_python-$VERSION-cp39-abi3-emscripten_3_1_58_wasm32.whl
uvx marimo@0.11.2 export html-wasm ./psp.py -o dist --mode edit
curl -L -o dist/public/$WHL https://github.com/finos/perspective/releases/download/v$VERSION/$WHL