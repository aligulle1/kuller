# -*- coding: utf-8 -*-
from comar.service import *

serviceType="server"
serviceDesc = _({"en": "Mumble Server",
                 "tr": "Mumble Sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/murmurd",
                 pidfile="/var/run/murmurd.pid",
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/murmurd",
                donotify=True)

    try:
        os.unlink("/var/run/murmurd.pid")
    except:
        pass

def status():
    return isServiceRunning(command="/usr/sbin/murmurd")
