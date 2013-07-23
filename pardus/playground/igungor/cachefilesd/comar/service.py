from comar.service import *

serviceType = "local"

serviceDesc = _({"en": "Start up and shut down the cachefilesd daemon",
                 "tr": "cachefilesd servisini açar ve kapatır"
                 })

serviceDefault = "off"

ERR_INSMOD = _({"en": "Failed probing module %s",
               "tr": "%s modülü yüklenemedi",
               })

PIDFILE = "/var/run/cachefilesd.pid"

@synchronized
def start():
    if run("/sbin/modprobe -q cachefiles"):
        fail(ERR_INSMOD % "cachefiles")

    startService(command="/usr/bin/cachefilesd",
                 pidfile=PIDFILE,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
