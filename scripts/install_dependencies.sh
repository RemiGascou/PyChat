#!/bin/bash

if [ "$(id -u)" != "0" ]; then
	echo "You need to be root to run this script. Try \"sudo\""
	exit 1
fi

sudo -H python3 -m pip install --upgrade pip
sudo -H python3 -m pip install PyQt5
sudo apt-get install python3-pyqt5
