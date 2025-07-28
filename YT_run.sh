#!/bin/bash

# Get the directory where the original script is located (not the symlink)
SCRIPT_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"

# Change to the project directory and run with uv
cd "$SCRIPT_DIR" && uv run main.py "$@"
