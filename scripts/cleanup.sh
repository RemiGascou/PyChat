#!/bin/bash

basedir="~/Documents/git_projects/PyChat/"
cd $basedir
cd ../lib
for dir in $(find "$basedir" -mindepth 1 -type d); do
		if [[ $dir == *"__pycache__" ]]; then
			echo "Removing" $dir
			rm -rf $dir
		fi
done
