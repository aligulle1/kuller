serviceType = "server"
serviceDesc = _({"en": "Bacula Backup Server",
                 "tr": "Bacula Yedek Sunucusu"})

from comar.service import *

@synchronized
def start():
    startService(command="/etc/bacula/bacula-ctl-fd",
                 args="start",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/etc/bacula/bacula-ctl-fd",
                args="stop",
                donotify=True)

def status():
    return isServiceRunning(pidFile="/var/run/bacula-fd.9102.pid",command="/etc/bacula/bacula-ctl-fd")
