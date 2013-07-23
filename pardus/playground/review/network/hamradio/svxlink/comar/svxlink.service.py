#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Amateur Radio Repeater Server",
                 "tr": "Amatör Radyo Röle Sunucusu"
                })

PID_FILE = "/var/run/svxlink.pid"
LOG_FILE = "/var/log/svxlink.log"
CONFIG_FILE = "/etc/svxlink/svxlink.conf"

@synchronized
def start():
    startService(command="/usr/bin/svxlink",
                 args="--pidfile=%s \
                       --logfile=%s \
                       --config=%s \
                       --runasuser=svxlink \
                       --daemon" % (PID_FILE, LOG_FILE, CONFIG_FILE))

@synchronized
def stop():
    stopService(pidfile=PID_FILE,
                donotify=True)

def status():
    return isServiceRunning(PID_FILE)

