import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "RAID monitor daemon",
                 "tr": "RAID izleme servisi"})
serviceConf = "mdadm"

def start():
    ret = run("mdadm --monitor --scan --daemonise -pid-file /var/run/mdadm.pid %s" % config.get("MDADM_OPTS"))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --pidfile /var/run/mdadm.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/mdadm.pid")
