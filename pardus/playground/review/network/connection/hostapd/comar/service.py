# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "IEEE 802.11 Access point daemon",
                 "tr": "IEEE 802.11 Erişim noktası hizmeti"})
serviceDefault = "off"

PROG="/usr/sbin/hostapd"
PIDFILE="/var/run/hostapd.pid"

@synchronized
def start():
    startService(command=PROG,
                 args="-B -P %s /etc/hostapd/hostapd.conf" % PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(pidfile=PIDFILE)
