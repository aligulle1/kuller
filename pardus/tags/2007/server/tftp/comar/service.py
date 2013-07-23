import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "TFTP Daemon",
                 "tr": "TFTP Sunucusu"})

def start():
    ret = run("/usr/sbin/in.tftpd -s -l /tftpboot")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --exec /usr/sbin/in.tftpd")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
