#!/bin/bash


##################################
## CLAUDEcho, © Niccolò Bianchi ##
##################################

## This CLI for a simple client-server with Anthropic's API for 
## Claude is the fork of another similar tool I made for OpenAI's
## API for chatgpt.


# check for required dependencies
REQUIRED_CMDS=("pyenv" "grep" "curl" "tar")

for cmd in "${REQUIRED_CMDS[@]}"; do
    if ! command -v "$cmd" &> /dev/null; then
        echo "Error: $cmd is not installed. Please install it and try again."
        exit 1
    fi
done

# specify Python version and virtual environment name
PYTHON_VERSION="3.12.0"
VENV_NAME="claudecho"
REQUIREMENTS="typer anthropic python-dotenv"

# check if the specified Python version is installed in pyenv
if ! pyenv versions | grep -q "$PYTHON_VERSION"; then
    echo "Python $PYTHON_VERSION is not installed. Installing with pyenv..."
    pyenv install $PYTHON_VERSION
fi

# check if the specified virtual environment exists
if ! pyenv virtualenvs | grep -q "$VENV_NAME"; then
    echo "Virtual environment '$VENV_NAME' does not exist. Creating with pyenv-virtualenv..."
    pyenv virtualenv $PYTHON_VERSION $VENV_NAME
else
    echo "Virtual environment '$VENV_NAME' already exists."
fi

# dynamically retrieve the path to the Python executable in the virtual environment
PYTHON_PATH=$(pyenv root)/versions/$VENV_NAME/bin/python

# check and install any missing packages
for package in $REQUIREMENTS; do
    if ! "$PYTHON_PATH" -m pip show "$package" > /dev/null 2>&1; then
        echo "Installing missing package: $package"
        "$PYTHON_PATH" -m pip install "$package"
    fi
done

# run the Python script
"$PYTHON_PATH" main.py "$@"


