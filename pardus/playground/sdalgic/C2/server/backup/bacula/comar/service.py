# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDefault = "off"
serviceDesc = _({"en": "Bacula Backup Server",
                 "tr": "Bacula Yedek Sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/bacula",
                 args="start",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/bacula",
                args="stop",
                donotify=True)

def status():
    return isServiceRunning(pidFile="/var/run/bacula/bacula.pid",command="/usr/sbin/bacula")
