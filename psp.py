#!/usr/bin/env -S uvx marimo@0.11.2 edit --sandbox
# /// script
# requires-python = "==3.13"
# dependencies = [
#     "marimo==0.11.2",
#     "perspective-python==3.3.4",
# ]
# ///

import marimo

__generated_with = "0.11.2"
app = marimo.App(width="full")


@app.cell
async def _():
    import sys 
    if "pyodide" in sys.modules:
        import micropip
        await micropip.install("http:/public/perspective_python-3.3.4-cp39-abi3-emscripten_3_1_58_wasm32.whl")
    import perspective
    psp_table = perspective.table("name,age\naszen,99")
    print(psp_table.schema())
    return micropip, perspective, psp_table, sys

if __name__ == "__main__":
    app.run()
