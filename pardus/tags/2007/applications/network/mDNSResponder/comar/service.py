from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Zeroconf Daemon",
                 "tr": "Zeroconf İstemcisi"})
serviceDefault = "on"

def start():
    call("System.Service.start", "sysklogd")
    ret = run("/sbin/start-stop-daemon --start -q --pidfile /var/run/mdnsd.pid --exec /usr/sbin/mdnsd")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop -q --pidfile /var/run/mdnsd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/mdnsd.pid")
