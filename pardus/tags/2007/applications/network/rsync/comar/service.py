serviceType = "server"
serviceDesc = _({"en": "RSync Daemon",
                 "tr": "RSync Sunucusu"})
serviceConf = "rsyncd"

from comar.service import *

def start():
    ret = run("rsync --daemon %s" % config.get("RSYNC_OPTS", ""))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --pidfile /var/run/rsyncd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/rsyncd.pid")
