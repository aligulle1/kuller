#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "local"
serviceDesc = _({
    "en": "Slim Login Manager",
    "tr": "Slim Giriş Yöneticisi",
})

@synchronized
def start():
    startService(command="/usr/bin/slim",
                 makepid=True,
                 detach=True,
                 pidfile="/var/run/slim.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/slim.pid",
                donotify=True)

def status():
    return isServiceRunning(pidfile="/var/run/slim.pid")
