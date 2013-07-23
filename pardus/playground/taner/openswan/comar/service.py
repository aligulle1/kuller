# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "IPSec Service",
                 "tr": "IPSec Servisi"})

@synchronized
def start():
    startService(command="/usr/sbin/ipsec",
                 args="setup --start",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/ipsec",
                args="setup --stop",
                donotify=True)

def status():
    return isServiceRunning("/var/run/pluto/pluto.pid")
