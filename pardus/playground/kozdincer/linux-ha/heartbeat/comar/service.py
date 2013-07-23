#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Heartbeat Daemon",
                 "tr": "Heartbeat Servisi"})

PIDFILE = "/var/run/heartbeat.pid"

@synchronized
def start():
    startService(command="/etc/init.d/heartbeat",
                 args="start",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/etc/init.d/heartbeat",
                args="stop",
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
