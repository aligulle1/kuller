import os
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "EciADSL Daemon",
                 "tr": "EciADSL Yöneticisi"})

def start():
    ret = run("/usr/bin/eciadsl-start")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/usr/bin/eciadsl-stop")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
