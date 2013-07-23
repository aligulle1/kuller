#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *


serviceType = "server"
serviceDesc = _({"en": "openerp server",
                 "tr": "openerp sunucusu"})

serviceDefault = "on"

@synchronized
def start():
    startDependencies("postgresql_server")

    startService(command="/usr/bin/openerp-server",
                 args="-c /etc/openerp-server/openerp-server.conf",
                 pidfile="/var/run/openerp-server/openerp-server.pid",
                 makepid=True,
                 detach=True,  
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/openerp-server",
                pidfile="/var/run/openerp-server/openerp-server.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/openerp-server/openerp-server.pid")

def reload():
    stopService(command="/usr/bin/openerp-server",
                args="reload")