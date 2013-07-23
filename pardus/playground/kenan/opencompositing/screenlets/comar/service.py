from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Screenlets Daemon",
                 "tr": "Screenlets Sunucusu"})

@synchronized
def start():
    startService(command="/usr/bin/screenletsd",
                 pidfile="/var/run/screenletsd.pid",
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/screenletsd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/screenletsd.pid")
