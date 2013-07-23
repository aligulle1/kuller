# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Cherokee Web Service",
                 "tr": "Cherokee Web Servisi"})

PIDFILE="/var/run/cherokee.pid"

@synchronized
def start():
    startService(command="/usr/sbin/cherokee",
                 pidfile=PIDFILE,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
