#!/bin/bash


echo "Cleaning .bzr directories.."
find . -depth -name .bzr -type d -exec rm -rf {} \;
find . -depth -name .bzrignore -type f -exec rm -rf {} \;
# Remove the execute bit from files that don't start with #!
for file in `find -type f -perm /111`; do
    if head -1 $file | egrep -v '^\#!' &>/dev/null; then
        echo "Removing +x bit from $file"
        chmod a-x $file
    fi
done
# Ensure shebang shell scripts have executable bit set
for file in `find -type f -perm /664`; do
    if head -1 $file | egrep '^\#!' &>/dev/null; then
        echo "Setting a+x bits for $file"
        chmod a+x $file
    fi
done
