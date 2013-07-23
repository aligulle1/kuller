serviceType = "server"
serviceDesc = _({"en": "Enlightened Sound Daemon",
                 "tr": "Enlightened Ses Sunucusu"})
serviceConf = "esound"

from comar.service import *

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --background \
               --exec /usr/bin/esd -- %s %s" % (config.get("ESD_START", ""), 
                                                config.get("ESD_OPTIONS", "")))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --exec /usr/bin/esd")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
