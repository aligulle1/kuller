from comar.service import *

serviceType = "local"
serviceDesc = "Portmap"

def start():
    config = loadConfig()
    opts = ""
    if "PORTMAP_OPTS" in config:
        opts = "-- %s" % config["PORTMAP_OPTS"]

    ret = run("/sbin/start-stop-daemon --start --quiet --make-pidfile --pidfile=/var/run/portmap.pid --exec /sbin/portmap %s" % opts)
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --exec /sbin/portmap")
    if ret == 0:
        os.unlink("/var/run/portmap.pid")
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/portmap.pid")
