#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for d in ["/var/lib/mtdaapd", "/var/lib/mtdaapd/playlists", "/var/log/mtdaapd", "/var/run/mtdaapd", "/var/db/mtdaapd", "/var/state/mtdaapd"]:
        if not os.path.exists(d):
            os.mkdir(d)
            # $ id nobody
            # uid=250(mpd) gid=18(audio)
            os.chown(d, 250, 18)
            os.chmod(d, 0750)

