#!/bin/bash

sudo curl -LsSf https://astral.sh/uv/install.sh | sh
# Issues with uv displaying options when ran rather than executing the script

# Create a persistent alias with a comment in the terminal
echo "" >> ~/.bashrc
echo "# Creating an alias for Youtube terminal video selection" >> ~/.bashrc
echo alias YT="'uv run main.py'" >> ~/.bashrc

# Symlink might not work due to python not knowing where to import modules from if not ran in project directory
sudo ln -s "$PWD/main.py" ~/.local/bin/

chmod +x $HOME/.local/bin/main.py


