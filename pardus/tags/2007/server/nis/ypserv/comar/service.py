import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Network Information Server",
                 "tr": "Ağ Bilgi Sunucusu (NIS)"})

def start():
    call("System.Service.start", "portmap")

    opts = ""
    if "YPSERV_OPTS" in config:
        opts = "-- %s" % config["YPSERV_OPTS"]

    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/ypserv %s" % opts)
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/ypserv")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/ypserv.pid")
