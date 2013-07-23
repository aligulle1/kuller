# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "ABRT Kernel Log Watcher",
                 "tr": "ABRT Çekirdek Günlük İzleyicisi"
                 })

PID_FILE="/var/run/abrt-dump-oops.pid"

@synchronized
def start():
    startService(command="/usr/bin/abrt-dump-oops",
                 args="-d /var/spool/abrt -rwx /var/log/messages",
                 pidfile=PID_FILE,
                 makepid=True,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PID_FILE,
                donotify=True)

def status():
    return isServiceRunning(PID_FILE)
