from comar.service import *
import os

serviceType = "server"
serviceDesc = _({"en": "GNU Krell Monitor Daemon",
                 "tr": "GNU Krell Sistem Takibi Sunucusu"})

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --background --pidfile /var/run/gkrellmd.pid --make-pidfile --exec /usr/bin/gkrellmd")

    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile /var/run/gkrellmd.pid --name gkrellmd")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/gkrellmd.pid")
