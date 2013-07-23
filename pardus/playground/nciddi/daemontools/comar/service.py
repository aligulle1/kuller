from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "Svscan Daemon",
                 "tr": "Svscan Sunucusu"})

@synchronized
def start():
    startService(command="/usr/bin/svscan",
                 args="/service",
                 pidfile="/var/run/svscan.pid",
                 makepid=True,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    for _svc in os.listdir("/service"):
        run("/usr/bin/svc -dx /service/%s" %_svc)
        run("/usr/bin/svc -dx /service/%s/log" %_svc)
    stopService(command="/usr/bin/svscan",
                 pidfile="/var/run/svscan.pid",
                 donotify=True)

def status():
    return isServiceRunning("/var/run/svscan.pid")
