#! /usr/bin/env bash

sudo apt update && sudo apt upgrade -y
sudo apt install -y nano vim python-is-python3 python3-venv python3-pip

python -m venv /home/vagrant/.my_venv
source /home/vagrant/.my_venv/bin/activate

pip install flask
flask --app /vagrant/hello.py run --host=0.0.0.0