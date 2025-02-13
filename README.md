# Using perspective with Marimo

Sample code to run perspective python in the browser (via Pyodide and Marimo)

## Requirements

- Install [UV](https://docs.astral.sh/uv/)

## Commands

`./psp.py` to run the notebook in normal python

`./build.sh` -> Builds notebook assets in `dist` and embeds perspective wasm whl.

`uvx python@3.13 -m http.server --directory=dist` -> Runs the wasm notebook in the browser

## Links

- [Perspective](https://perspective.finos.org/)
- [Marimo.io](https://marimo.io/)
- [Pyodide](https://pyodide.org/en/stable/)
