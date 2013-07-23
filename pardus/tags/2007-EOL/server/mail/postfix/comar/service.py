import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Postfix Mail Server",
                 "tr": "Postfix E-Posta Sunucusu"})

def start():
    ret = run("/usr/sbin/postfix", "start")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/usr/sbin/postfix", "stop")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to start service")

def reload():
    ret = run("/usr/sbin/postfix", "reload")
    if ret == 0:
        notify("System.Service.changed", "reloaded")
    else:
        fail("Unable to reload service")
