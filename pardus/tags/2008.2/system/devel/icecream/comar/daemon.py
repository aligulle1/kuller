import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Icecream Daemon",
                 "tr": "Icecream Sunucusu"})

def start():
    ret = run("/sbin/start-stop-daemon --start \
               --pid /var/run/iceccd.pid \
               --quiet --exec /opt/icecream/sbin/iceccd -- -d -m 5 > /dev/null")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop \
               --quiet --retry 5 \
               --exec /opt/icecream/sbin/iceccd")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/iceccd.pid")
