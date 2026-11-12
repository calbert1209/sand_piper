#!/bin/bash

##
# HINT: http://www.movingelectrons.net/posts/circuitpython-and-version-control/
##

# Text file holding filenames and folders to be excluded
excluded_files=".rsyncignore"

# Use the current directory as the source folder
source_folder="."

# Check if the destination folder argument is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <destination_folder>"
  exit 1
fi

# Set the destination folder variable to the first argument
destination_folder="$1"

# Check if destination folder exists
if [[ ! -d "$destination_folder" ]]; then
    echo "Error: destination folder '$destination_folder' not found."
    exit 1
fi

# Use rsync to copy files (using flags friendly to FAT filesystems on CIRCUITPY)
rsync -rtv --delete --modify-window=1 --progress "$source_folder/" "$destination_folder/" --exclude-from="$excluded_files"

