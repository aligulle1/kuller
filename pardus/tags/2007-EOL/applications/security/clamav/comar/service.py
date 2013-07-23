import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Clam Anti-Virus Daemon",
                 "tr": "Clam Anti-Virüs Sunucusu"})

@synchronized
def start():
    if config.get("DAZUKO_SUPPORT", "no") == "yes":
                call("System.Service.start", "dazuko")

    startService(command="/usr/sbin/clamd",
                         pidfile="/var/run/clamav/clamd.pid",
                         donotify=True)
    startService(command="/usr/bin/freshclam",
                         args="-d")

@synchronized
def stop():
    stopService(command="/usr/sbin/clamd",
                        donotify=True)
    time.sleep(3)
    stopService(command="/usr/bin/freshclam")
    call("System.Service.stop", "dazuko")

def status():
    return isServiceRunning(command="/usr/sbin/clamd")
