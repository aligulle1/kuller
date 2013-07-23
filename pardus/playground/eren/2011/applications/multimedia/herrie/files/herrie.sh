#!/bin/bash

# A wrapper script for herrie. Herrie automatically saves playlists to ~/.herrie/playlist.xspf but ~/.herrie doesn't exist by default and herrie doesn't create that directory. Control whether ~/.herrie exits and create it if doesn't.

if [ ! -e ~/.herrie ]
then
    mkdir ~/.herrie
fi

exec herrie-bin $*
