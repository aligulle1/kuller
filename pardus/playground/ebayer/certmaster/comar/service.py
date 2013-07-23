#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "certificate master for FUNC",
                 "tr": "FUNC aracı için sertifika yöneticisi"})

from comar.service import *

@synchronized
def start():
    startService(command="/usr/bin/certmaster",
                 args="--daemon",
                 donotify=True)

@synchronized
def stop():
    stopService("/var/run/certmaster.pid")

def status():
    return isServiceRunning("/var/run/certmaster.pid")
