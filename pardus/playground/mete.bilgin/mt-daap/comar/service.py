#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Music Player Daemon",
                 "tr": "Müzik Çalıcı Sunucusu"})

from comar.service import *
import re
import os

pidfile = "/var/run/mt-daapd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/mt-daapd",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile,
                donotify=True)

def status():
    return isServiceRunning(pidfile)
