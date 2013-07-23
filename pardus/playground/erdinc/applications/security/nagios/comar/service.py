import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Nagios Daemon",
                 "tr": "Nagios Sunucusu"})

@synchronized
def start():
    call("System.Service.start", "apache")
    startService(command="/usr/nagios/bin/nagios",
                         pidfile="/var/nagios/nagios.lock",
                         args="-d /etc/nagios/nagios.cfg",
                         donotify=True)
@synchronized
def stop():
    stopService(pidfile="/var/nagios/nagios.lock",
                donotify=True)

def status():
    return isServiceRunning("/var/nagios/nagios.lock")
