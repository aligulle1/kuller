from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "QEMU and virtual network management daemon",
                 "tr": "QEMU and virtual network management daemon"})
serviceDefault = "off"

@synchronized
def start():
    startService(command="/usr/sbin/libvirtd",
                 args="--daemon",
                 pidfile="/var/run/libvirtd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/libvirtd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/libvirtd.pid")
