# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Connection Manager",
                 "tr": "Bağlantı Yöneticisi"})
serviceDefault = "off"

PIDFILE="/var/run/connman/connman.pid"

@synchronized
def start():
    startService(command="/usr/sbin/connmand",
                 args="-n",
                 detach=True,
                 makepid=True,
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

    try:
        os.unlink(PIDFILE)
    except:
        pass

def status():
    return isServiceRunning(PIDFILE)
