import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Clam Anti-Virus Daemon",
                 "tr": "Clam Anti-Virüs Sunucusu"})

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/clamd --pidfile /var/run/clamav/clamd.pid")
    ret += run("/sbin/start-stop-daemon --start --quiet --exec /usr/bin/freshclam -- -d")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/clamd --p /var/run/clamav/clamd.pid")
    ret += run("/sbin/start-stop-daemon --stop --quiet --name freshclam")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/clamav/clamd.pid")
