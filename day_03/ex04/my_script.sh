#!/bin/bash

# setup venv
python3 -m virtualenv django_venv
source django_venv/bin/activate

# pip version
pip3 --version

# pip install
pip3 install --upgrade pip
pip3 install --log install.log --upgrade --force-reinstall -r requirement.txt