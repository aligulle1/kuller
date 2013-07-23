from comar.service import *
import os

serviceType = "script"
serviceDesc = _({"en": "HSF Modem Manager",
                 "tr": "HSF Modem Yöneticisi"})

def start():
    if os.path.exists("/dev/ttySHSF0") and not os.path.exists("/dev/modem"):
        os.symlink("ttySHSF0", "/dev/modem")

    ret = run("/usr/sbin/hsfconfig --rcstart")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/usr/sbin/hsfconfig --rcstop")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
