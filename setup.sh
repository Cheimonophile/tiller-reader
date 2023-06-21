#!/bin/sh -xe

# python
pyenv exec python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

