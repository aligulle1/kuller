serviceType = "server"
serviceDesc = _({"en": "Cyrus-SASL Daemon",
                 "tr": "Cyrus-SASL Sunucusu"})
serviceConf = "saslauthd"

import os
from comar.service import *

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/saslauthd -- %s" % config.get("SASLAUTHD_OPTS", ""))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile /var/lib/sasl2/saslauthd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/lib/sasl2/saslauthd.pid")
