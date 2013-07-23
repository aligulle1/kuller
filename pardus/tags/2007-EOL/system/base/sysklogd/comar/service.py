from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "System Message Logger",
                 "tr": "Sistem Mesajları Kütüğü"})
serviceDefault = "on"

@synchronized
def start():
    reply = startService(command="/usr/sbin/syslogd",
                         args="-m 15",
                         pidfile="/var/run/syslogd.pid",
                         detach=True,
                         donotify=True)
    if reply == 0:
        waitBus("/dev/log", stream=False)
        startService(command="/usr/sbin/klogd",
                     args="-c 3 -2",
                     detach=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/klogd.pid")
    stopService(pidfile="/var/run/syslogd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/syslogd.pid")
