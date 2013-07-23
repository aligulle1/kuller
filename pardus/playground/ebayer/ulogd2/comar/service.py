#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "The userspace logging daemon for netfilter",
                 "tr": "Netfilter kayıt günlüğü servisi"})

from comar.service import *

@synchronized
def start():
    startService("/usr/sbin/ulogd",
                 args="-d", donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/ulogd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/ulogd")
