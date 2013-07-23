from comar.service import *
import os

serviceType = "script"
serviceDesc = _({"en": "HCF Modem Manager",
                 "tr": "HCF Modem Yöneticisi"})

def start():
    if os.path.exists("/dev/ttySHCF0") and not os.path.exists("/dev/modem"):
        os.symlink("ttySHCF0", "/dev/modem")

    ret = run("/usr/sbin/hcfpciconfig --rcstart")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/usr/sbin/hcfpciconfig --rcstop")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
