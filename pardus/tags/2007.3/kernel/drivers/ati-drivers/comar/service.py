serviceType = "local"
serviceDesc = _({"en": "Atievents Daemon",
                 "tr": "Atievents Sunucusu"})
serviceConf = "atieventsd"

from comar.service import *

@synchronized
def start():
    startService(command="/opt/ati/sbin/atieventsd",
                 args=config.get("ATIEVENTSDOPTS", ""),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/opt/ati/sbin/atieventsd",
                donotify=True)

def status():
    return isServiceRunning(command="/opt/ati/sbin/atieventsd")
