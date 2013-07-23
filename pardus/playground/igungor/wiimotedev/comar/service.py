# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "WiiMoteDev Daemon",
                 "tr": "WiiMoteDev Sunucu"})

serviceConf = "wiimotedev"

PIDFILE = "/var/run/wiimotedev-daemon.pid"

@synchronized
def start():
    startService(command="/usr/sbin/wiimotedev-daemon",
                 args="--no-daemon",
                 detach=True,
                 makepid=True,
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
