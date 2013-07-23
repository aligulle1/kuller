#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Zabbix server daemon",
                 "tr": "Zabbix sunucusu"})

from comar.service import *

@synchronized
def start():
    startService("/usr/sbin/zabbix_server_sqlite",
                 chuid="zabbix:zabbix", donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/zabbix/zabbix.pid")

def status():
    return isServiceRunning("/var/run/zabbix/zabbix.pid")
