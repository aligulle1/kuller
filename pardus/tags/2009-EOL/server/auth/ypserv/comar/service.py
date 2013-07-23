from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Network Information Server",
                 "tr": "Ağ Bilgi Sunucusu (NIS)"})

@synchronized
def start():
    startDependencies("portmap")
    startService(command="/usr/sbin/ypserv",
                 args=config.get("YPSERV_OPTS", ""),
                 pidfile="/var/run/ypserv.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/ypserv.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/ypserv.pid")
