#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Svxlink Remote Transceiver Service",
                 "tr": "Svxlink Uzak Alıcı/Verici Servisi"
                })

PID_FILE = "/var/run/remotetrx.pid"
LOG_FILE = "/var/log/remotetrx.log"
CONFIG_FILE = "/etc/svxlink/remotetrx.conf"

@synchronized
def start():
    startService(command="/usr/bin/remotetrx",
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

