#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType="server"
serviceDesc = _({"en": "Firebird Database Server",
                 "tr": "Firebird Veritabanı Sunucusu"})

from comar.service import *

pid_file = "/var/run/firebird/firebird.pid"
manager = "/opt/firebird/bin/fbmgr.bin"

def start():
    ret = run("/sbin/start-stop-daemon --oknodo --start --pidfile %s --chuid firebird --startas %s -- -pidfile %s -start -forever" % (pid_file, manager, pid_file))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --pidfile %s --oknodo" % pid_file)
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon(pid_file)
