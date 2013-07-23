# -*- coding: utf-8 -*-
serviceType = "local"
serviceDesc = _({"en": "APM Daemon",
                 "tr": "APM Servisi"})

from comar.service import *

@synchronized
def start():
    import os
    if not os.path.exists("/proc/apm"):
        fail("APM not found")

    startService(command="/usr/sbin/apmd",
                 args=config.get("APMD_OPTS", ""),
                 pidfile="/var/run/apmd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/apmd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/apmd.pid")
