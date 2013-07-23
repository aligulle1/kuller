#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall():
    os.system("chmod 740 /etc/mpd.conf")
    if not os.path.exists("/var/lib/mpd") or not os.path.exists("/var/log/mpd"):
        os.mkdir("/var/lib/mpd")
        os.mkdir("/var/lib/mpd/playlists")
        os.mkdir("/var/log/mpd")
