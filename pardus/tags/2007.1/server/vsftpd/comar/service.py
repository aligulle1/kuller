import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "vsFTP Daemon",
                 "tr": "vsFTP Sunucusu"})

def start():
    if 0 != run("/sbin/modprobe capability"):
        fail("cannot load capability module")
    ret = run("start-stop-daemon --start --exec /usr/sbin/vsftpd --background --make-pidfile --pidfile /var/run/vsftpd.pid -- /etc/vsftpd/vsftpd.conf")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --exec /usr/sbin/vsftpd --pidfile /var/run/vsftpd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/vsftpd.pid")
