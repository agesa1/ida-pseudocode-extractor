# ida-pseudocode-extractor

# IDA Pro Hex-Rays Automatic Decompiler & Function Exporter

This script automatically decompiles every function in a loaded binary using IDA Pro + Hex-Rays, removes IDA color tags, and exports each function’s pseudocode into a separate `.txt` file.

## Features
- Iterates through all functions in the database
- Decompiles each function using Hex-Rays
- Cleans IDA color tags for clean readable output
- Saves each function into its own file: `FunctionName.txt`
- Creates the output directory if it does not exist
- Reports all successful and failed decompilations

## Output
All generated pseudocode files are written to the directory specified in `output_dir`.


## Requirements
- IDA Pro with a valid Hex-Rays Decompiler license
- IDA Python environment (built-in)

## Usage
1. Set the desired output directory in the script (`output_dir`).
2. Load a binary in IDA Pro.
3. Run the script via: `File → Script file...`
4. All functions will be automatically decompiled and exported.
