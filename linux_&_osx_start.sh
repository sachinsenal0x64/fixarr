#!/bin/sh

git clone https://github.com/sachinsenal0x64/FIXARR
cd FIXARR
echo "Installing Packages......"
pip install -r requirements.txt
python fixarr.py
