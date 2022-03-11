#!/bin/bash

sudo apt update -y
sudo apt install python3-pip
pip3 install -r requirements.txt
python3 client/client.py
