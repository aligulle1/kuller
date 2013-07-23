from comar.service import *

serviceType = "local"
serviceDesc = "Portmap"

@synchronized
def start():
    startService(command="/sbin/portmap",
                 args=config.get("PORTMAP_OPTS", ""),
                 pidfile="/var/run/portmap.pid",
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    reply = stopService(pidfile="/var/run/portmap.pid",
                        donotify=True)
    if reply == 0:
        import os
        os.unlink("/var/run/portmap.pid")

def status():
    return isServiceRunning("/var/run/portmap.pid")
