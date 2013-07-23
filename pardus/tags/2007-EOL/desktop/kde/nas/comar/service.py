serviceType = "server"
serviceDesc = _({"en": "Network Audio System", 
                 "tr": "Ağ Ses Sistemi"})
serviceConf = "nas"

from comar.service import *

def start():

    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/bin/nasd \
               --background --pidfile /var/run/nasd.pid --make-pidfile \
               -- %s" % config.get("NAS_OPTIONS", ""))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile /var/run/nasd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/nasd.pid")
