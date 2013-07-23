#!/bin/sh
#
# extract_components.sh - a simple sh script to find component of a
#                         package due to your pisi repo in your system.
#
# Sample usage:
#     > extract_components pisi
#     system/base/pisi
#
# Serdar Dalgic
# serdar AT pardus DOT org DOT tr
#

var1=`LC_ALL=C pisi info $1 | grep Component | grep -v unknown | uniq | cut -d":" -f2`

echo $var1/$1 | sed "s/\./\//g"
