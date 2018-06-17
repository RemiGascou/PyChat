#!/bin/bash

#Check if root
if [ "$(id -u)" != "0" ]; then
	echo "Couldn't run script. Try again with \"sudo ./upgrade.sh\" "
	exit 1
fi

git status
git pull
