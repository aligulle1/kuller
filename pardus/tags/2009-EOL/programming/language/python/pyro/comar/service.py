# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Pyro Name Server Daemon"})

@synchronized
def start():
    startService(command="/usr/bin/pyro-nsd",
            args="start",
            donotify=True,
            detach=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/pyro-nsd.pid",
            donotify=True)

def status():
    return isServiceRunning("/var/run/pyro-nsd.pid")
