from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Policy Kit",
                 "tr": "Politika Araçları"})
serviceDefault = "on"

def start():
    ret = run("/sbin/start-stop-daemon --start -q --exec /usr/sbin/polkitd")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop -q --pidfile /var/run/polkit-console/polkit.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/polkit-console/polkit.pid")
