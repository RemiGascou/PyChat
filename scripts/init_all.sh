#!/bin/bash

FORCE=0
RUNNING=1
CLEANUPONLY=1

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

case $key in
    -f|--force)
    FORCE=1
		echo -e "\x1b[1m[\x1b[0m\x1b[1;91mwarn\x1b[0m\x1b[1m]\x1b[0m All __init__.py will be overwritten."
    shift # past argument
    shift # past value
    ;;
    -h|--help)
    RUNNING=0
		echo -e "\x1b[1mUsage :\x1b[0m"
		echo -e "      \x1b[1m-c, --clean-only\x1b[0m : Only cleans project. (Remove all __pycache__)"
		echo -e "      \x1b[1m-f, --force\x1b[0m : Force overwritting all __init__.py."
		echo -e "      \x1b[1m-h, --help\x1b[0m  : Display help."
    shift # past argument
    shift # past value
    ;;
		-c|--clean-only)
    CLEANUPONLY=1
		echo -e "\x1b[1m[\x1b[0m\x1b[1;91mwarn\x1b[0m\x1b[1m]\x1b[0m All __init__.py will be overwritten."
    shift # past argument
    shift # past value
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters


if [[ $CLEANUPONLY != 0 ]]; then
	basedir="/home/tux/Documents/git_projects/PyChat/"
	cd $basedir
	for dir in $(find "$basedir" -mindepth 1 -type d); do
			if [[ $dir == *"__pycache__" ]]; then
				echo "Removing" $dir
				rm -rf $dir
			fi
	done
fi

if [[ $RUNNING != 0 ]]; then
	basedir="/home/tux/Documents/git_projects/PyChat/lib"
	cd $basedir
	for dir in $(find "$basedir" -mindepth 1 -type d); do
		pos=`expr ${#basedir} - ${#dir}`
		if [[ -f "__init__.py" ]]; then
			if [[$FORCE == 1]]; then
				rm __init__.py
			else
				echo "Existing file __init__.py for" ${dir:(pos)} "skipping..."
				continue
			fi
		else
			echo "Generating __init__.py for" ${dir:(pos)}
		  for e in $(find "$dir" -maxdepth 1 -type f -name '*.py' | sort -u); do
				e=$(basename $e)
				if [[ $e != "__"* ]]; then
						echo -e " [\x1b[1m+\x1b[0m] " ${e%.*}
				fi
		  done
		fi
	done
fi
