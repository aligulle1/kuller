# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDefault = "off"
serviceDesc = _({"en": "Bacula Backup Server File Deamon",
                 "tr": "Bacula Yedek Sunucusu Dosya Hizmeti"})

COMMAND = "/usr/sbin/bacula-fd"

@synchronized
def start():
    startService(command=COMMAND,
                 args="-c /etc/bacula/bacula-fd.conf",
                 donotify=True)

@synchronized
def stop():
    stopService(command=COMMAND,
                donotify=True)

def status():
    return isServiceRunning(command=COMMAND)
