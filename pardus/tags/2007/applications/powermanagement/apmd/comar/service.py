serviceType = "local"
serviceDesc = _({"en": "APM Daemon",
                 "tr": "APM Sunucusu"})

from comar.service import *
import os

def start():
    if not os.path.exists("/proc/apm"):
        fail("APM not found")
    else:
        ret = run("start-stop-daemon --start --quiet --pidfile /var/run/apmd.pid \
                   --startas /usr/sbin/apmd -- %s" % config.get("APMD_OPTS", ""))
        if ret == 0:
            notify("System.Service.changed", "started")
        else:
            fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --quiet --pidfile /var/run/apmd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/apmd.pid")
