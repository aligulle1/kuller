#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Music Player Daemon",
                 "tr": "Müzik Çalıcı Sunucusu"})

from comar.service import *
import re
import os

@synchronized
def start():
    conf = open("/etc/mpd.conf")

    # control if music_directory has been correctly set
    for line in conf.readlines():
        if line.startswith("music_directory"):
            regex = re.compile('"(.*?)"')
            music_dir = regex.search(line).groups()[0]

            if not os.path.exists(music_dir):
                fail('Music directory "%s" doesn\'t exist, please edit your /etc/mpd.conf and set a valid directory' % music_dir)

    conf.close()

    # flush mpd's db for re-walking directory if it's changed
    if os.path.exists("/var/lib/mpd/mpd.db"):
        os.unlink("/var/lib/mpd/mpd.db")

    startService(command="/usr/bin/mpd", detach=True, donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/mpd", args="--kill", donotify=True)

def status():
    return isServiceRunning("/var/run/mpd.pid")
