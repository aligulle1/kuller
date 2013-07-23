from comar.service import *

serviceType="server"
serviceDesc = _({"en": "Mediatomb UPnP Media Server",
                 "tr": "Mediatomb UPnP Ortam Sunucusu"})

@synchronized
def start():
    startService(command="/usr/bin/mediatomb",
                 args=config.get("MEDIATOMB_OPTS", ""),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/mediatomb/mediatomb.pid",
                donotify=True)

    try:
        os.unlink("/var/run/mediatomb/mediatomb.pid")
    except:
        pass

def status():
    return isServiceRunning("/var/run/mediatomb/mediatomb.pid")

