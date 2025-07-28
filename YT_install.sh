#!/bin/bash

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "uv not found. Installing..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    echo "uv installed successfully!"
else
    echo "uv is already installed."
fi

# Sync uv dependencies
uv sync

# Make the runner script executable
chmod +x YT_run.sh

# Create ~/.local/bin if it doesn't exist
mkdir -p ~/.local/bin

# Symlink to local bin so can be used from anywhere
ln -sf "$PWD/YT_run.sh" ~/.local/bin/YT_run.sh

echo "Installation complete!"
