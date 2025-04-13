#!/bin/bash

# create virtual environment
python3 -m venv .venv

# install dependencies
source .venv/bin/activate
pip3 install -r requirements.dev.txt

# setup git hooks
pre-commit install
