serviceType = "local"
serviceDesc = _({"en": "Atievents Daemon",
                 "tr": "Atievents Sunucusu"})
serviceConf = "atieventsd"

import os
from comar.service import *

def start():
    ret = run("/sbin/start-stop-daemon --start --pidfile /var/run/atieventsd.pid --exec /opt/ati/sbin/atieventsd \
               -- %s" % config.get("ATIEVENTSDOPTS", ""))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile /var/run/atieventsd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/atieventsd.pid")
