#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "System Message Logger",
                 "tr": "Sistem Mesajları Kütüğü"})
serviceDefault = "on"

@synchronized
def start():
    startService(command="/usr/sbin/rsyslogd",
                 args="-c3",
                 pidfile="/var/run/rsyslogd.pid",
                 detach=True)

    waitBus("/dev/log", stream=False)

@synchronized
def stop():
    stopService(pidfile="/var/run/rsyslogd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/rsyslogd.pid")

