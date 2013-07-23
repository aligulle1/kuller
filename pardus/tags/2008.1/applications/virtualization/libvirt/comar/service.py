from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "QEMU and virtual network management daemon",
                 "tr": "QEMU and virtual network management daemon"})
serviceDefault = "off"

@synchronized
def start():
    startService(command="/usr/bin/libvirt",
                 args="--daemon",
                 pidfile="/var/run/libvirt.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/libvirt.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/libvirt.pid")
