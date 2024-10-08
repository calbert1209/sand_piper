#!/bin/bash

##
# HINT: http://www.movingelectrons.net/posts/circuitpython-and-version-control/
##

# Text file holding filenames and folders to be excluded
excluded_files="excluded_files.txt"

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
    echo "Error: destination folder not found."
    exit 1
fi

# Use rsync to copy files
rsync -avz --progress "." "$destination_folder/" --exclude-from=.rsyncignore