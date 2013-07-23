serviceType = "server"
serviceDesc = _({"en": "HSQLDB Java SQL Server",
                 "tr": "HSQLDB Java SQL Sunucusu"})

from comar.service import *

@synchronized
def start():
    startService(command="/usr/sbin/hsqldb",
                 args="start",
                 pidfile="/var/run/hsqldb/hsqldb.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/hsqldb",
                args="stop",
                donotify=True)

def status():
    return isServiceRunning("/var/run/hsqldb/hsqldb.pid")
