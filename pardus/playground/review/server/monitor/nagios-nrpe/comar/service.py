#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Monitoring agent for Nagios",
                 "tr": "Nagios için izleme ajanı"})

from comar.service import *

@synchronized
def start():
    startService("/usr/sbin/nrpe",
                 args="-c /etc/nagios/nrpe.cfg -d %s" % config.get("NRPE_OPTS", ""),
                 donotify=True)

@synchronized
def stop():
    stopService("/var/run/nrpe/nrpe.pid", donotify=True)

def status():
    return isServiceRunning("/var/run/nrpe/nrpe.pid")
