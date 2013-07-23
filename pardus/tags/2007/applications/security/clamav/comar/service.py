import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Clam Anti-Virus Daemon",
                 "tr": "Clam Anti-Virus Sunucusu"})

def start():
    ret = run("start-stop-daemon --start --quiet --exec /usr/sbin/clamd")
    ret += run("start-stop-daemon --start --quiet --exec /usr/bin/freshclam")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --quiet --name clamd")
    ret += run("start-stop-daemon --stop --quiet --name freshclam")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
