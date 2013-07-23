# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"

serviceDesc = _({"en": "DHCPv6 Daemon",
                 "tr": "DHCPv6 Servisi"})

serviceConf = "dhcpd6"

PIDFILE = "/var/run/dhcpd6.pid"

@synchronized
def start():
    startService(command="/usr/sbin/dhcpd",
                 args="-6 %s %s" % (config.get("DHCPD_ARGS", ""), config.get("INTERFACES", "")),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/dhcpd",
                pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
