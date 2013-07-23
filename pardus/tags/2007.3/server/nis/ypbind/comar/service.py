import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "NIS Bind Service",
                 "tr": "NIS Bağlantı Servisi"})

def start():
    call("System.Service.start", "portmap")
    call("System.Service.start", "ypserv")

    opts = ""
    if "YPBIND_OPTS" in config:
        opts = "-- %s" % config["YPBIND_OPTS"]

    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/ypbind %s" % opts)
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/ypbind")

    if ret == 0:
        run("/usr/bin/rm -f /var/yp/binding/")
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
