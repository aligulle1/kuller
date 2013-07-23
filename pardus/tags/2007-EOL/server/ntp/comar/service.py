import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "NTP Daemon",
                 "tr": "NTP Sunucusu"})

def start():
    call("System.Service.start", "portmap")
    # Capabilities needed to drop root privileges
    run("/sbin/modprobe capability")
    ret = run("/usr/sbin/ntpd -p /var/run/ntpd.pid -u ntp:ntp")
    if ret == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("start-stop-daemon --stop --pidfile /var/run/ntpd.pid --exec /usr/sbin/ntpd")
    if ret == 0:
        notify("System.Service.changed", "stopped")

def status():
    return checkDaemon("/var/run/ntpd.pid")
