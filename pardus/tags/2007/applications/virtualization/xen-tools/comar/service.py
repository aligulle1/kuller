from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "XEN Daemon",
                 "tr": "XEN Suncusu"})
serviceDefault = "off"

def start():
    ret = run("/usr/sbin/xend start")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    run("/usr/sbin/xm shutdown --all --wait")
    ret = run("/usr/sbin/xend stop")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/xenstore.pid")
