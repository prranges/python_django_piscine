#!/bin/bash

# pip version
pip3 --version

# pip install
pip3 install git+https://github.com/jaraco/path.git --target local_lib --log install.log --force-reinstall --upgrade

# start my_program
python3 my_program.py
