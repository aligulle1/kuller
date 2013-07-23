import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "HylaFax Daemon",
                 "tr": "HylaFax Sunucusu"})

def start():
    ret = run("start-stop-daemon --start --quiet --exec /usr/sbin/hfaxd -- -i hylafax -o 4557 -s 444")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --quiet --exec /usr/sbin/hfaxd")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
