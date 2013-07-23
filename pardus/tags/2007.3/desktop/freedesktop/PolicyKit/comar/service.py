from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Policy Kit",
                 "tr": "Politika Araçları"})
serviceDefault = "on"

@synchronized
def start():
    startDependencies("dbus")

    startService(command="/usr/sbin/polkitd",
                 pidfile="/var/run/PolicyKit/pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/PolicyKit/pid",
                donotify=True)

def status():
    return isServiceRunning(pidfile="/var/run/PolicyKit/pid")
