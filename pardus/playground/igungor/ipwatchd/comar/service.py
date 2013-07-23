from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "IP conflict detection service",
                 "tr": "IP çakışmalarını algılayan bir servis"})
serviceDefault = "on"

PIDFILE = "/var/run/ipwatchd.pid"

@synchronized
def start():
    startService(command="/usr/sbin/ipwatchd",
                 args="-c /etc/ipwatchd.conf",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=PIDFILE,
                donotify=True)

def status():
    return isServiceRunning(PIDFILE)
