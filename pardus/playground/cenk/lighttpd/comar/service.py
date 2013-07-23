#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Lighttpd Web Server",
                 "tr": "Lighttpd Web Sunucusu"})

from comar.service import *

@synchronized
def start():
    startService(command="/usr/sbin/lighttpd", \
                 args="-f /etc/lighttpd/lighttpd.conf", \
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/lighttpd", \
                pidfile="/var/run/lighttpd/lighttpd.pid", \
                donotify=True)

def status():
    return isServiceRunning("/var/run/lighttpd/lighttpd.pid")
