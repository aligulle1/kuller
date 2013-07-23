#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Network intrusion prevention and detection system",
                 "tr": "Ağ saldırı önleme ve yakalama sistemi"})

from comar.service import *

@synchronized
def start():
    startService("/usr/bin/snort",
                 args="%s -i %s" % (config.get("DAEMON_OPTS"), config.get("DAEMON_IFACE")),
                 donotify=True)

@synchronized
def stop():
    stopService("/var/run/snort_%s.pid" % config.get("DAEMON_IFACE"))

def status():
    return isServiceRunning("/var/run/snort_%s.pid" % config.get("DAEMON_IFACE"))
