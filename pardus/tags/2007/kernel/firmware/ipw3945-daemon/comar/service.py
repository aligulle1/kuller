import os
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Intel Centrino wireless (ipw3945) regulator",
                 "tr": "Intel Centrino kablosuz ağ (ipw3945) düzenleyici"})

def start():
    ret = run("/sbin/ipw3945d")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/ipw3945d --kill")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    ret = run("/sbin/ipw3945d --isrunning")
    return ret == 0

def ready():
    s = get_profile("System.Service.setState")
    if s:
        state = s["state"]
        if state == "on":
            start()
    else:
        # If no user profile is set, autodetect the device
        # FIXME: this device check might be a good candidate for commar api call
        path = "/sys/bus/pci/devices"
        for name in os.listdir(path):
            vendor = file(os.path.join(path, name, "vendor")).read().rstrip("\n")
            device = file(os.path.join(path, name, "device")).read().rstrip("\n")
            if vendor == "0x8086":
                if device == "0x4222" or device == "0x4227":
                    start()
