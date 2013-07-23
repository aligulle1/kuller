from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "OpenVAS server",
                 "tr": "OpenVAS servisi"})

@synchronized
def start():
    startService(command="/usr/sbin/openvasd",
                 pidfile="/var/run/openvasd.pid",
                 detach=True,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/openvasd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/openvasd.pid")
