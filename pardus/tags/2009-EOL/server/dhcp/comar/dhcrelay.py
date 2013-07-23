# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"

serviceDesc = _({"en": "DHCP Relay Server",
                 "tr": "DHCP Relay Servisi"})

serviceConf = "dhcrelay"

PIDFILE = "/var/run/dhcrelay.pid"

@synchronized
def start():
    startService(command="/usr/sbin/dhcrelay",
                 args="%s %s" % (config.get("DHCPD_ARGS", ""), config.get("INTERFACES", "")),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/dhcpd",
                pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
