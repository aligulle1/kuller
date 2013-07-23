from comar.service import *
from time import sleep

serviceType = "server"
serviceDesc = _({"en": "ZoneMinder service",
                 "tr": "ZoneMinder servisi"})

@synchronized
def start():
    startDependencies("apache", "mysql_server")
    sleep(3)
    startService(command="/usr/bin/zmpkg.pl",
                 args="start",
                 pidfile="/var/run/zm/zm.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/zmpkg.pl",
                 args="stop",
                 donotify=True)

def status():
    return isServiceRunning("/var/run/zm/zm.pid")
