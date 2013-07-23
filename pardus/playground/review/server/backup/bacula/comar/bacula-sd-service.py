# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDefault = "off"
serviceDesc = _({"en": "Bacula Backup Server Storage Deamon",
                 "tr": "Bacula Yedek Sunucusu Depolama Hizmeti"})

COMMAND = "/usr/sbin/bacula-sd"
USER="bacula"
GROUP="bacula"

@synchronized
def start():
    startService(command=COMMAND,
                 args="-c /etc/bacula/bacula-sd.conf -u %s -g %s" %(USER, GROUP),
                 donotify=True)

@synchronized
def stop():
    stopService(command=COMMAND,
                donotify=True)

def status():
    return isServiceRunning(command=COMMAND)
