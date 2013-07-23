import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Slurpd Daemon",
                 "tr": "Slurpd Sunucusu"})

def start():
    ret = run("start-stop-daemon --start --quiet --exec /usr/libexec/slurpd")
    if ret == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("start-stop-daemon --stop --quiet --exec /usr/libexec/slurpd ")
    if ret == 0:
        notify("System.Service.changed", "stopped")
