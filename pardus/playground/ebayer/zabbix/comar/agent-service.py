#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Zabbix agent daemon",
                 "tr": "Zabbix ajan servisi"})

from comar.service import *

@synchronized
def start():
    startService("/usr/sbin/zabbix_agentd",
                 chuid="zabbix:zabbix", donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/zabbix/zabbix_agentd.pid")

def status():
    return isServiceRunning("/var/run/zabbix/zabbix_agentd.pid")
