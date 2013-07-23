#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Daemon version of kinit for Kerberos v5",
                 "tr": "Kerberos5 için kinit servisi"})

from comar.service import *

PIDFILE = "/var/run/k5start.pid"
DAEMON_OPTS = config.get("DAEMON_OPTS", "")

MSG_NM_NOT_RUNNING = _({"en": "NetworkManager service is not running",
                        "tr": "NetworkManager hizmeti çalışmıyor",
                       })
@synchronized
def start():
    if run("/usr/bin/nm-online -q -t 10") != 0:
        # NM is not running
        fail(MSG_NM_NOT_RUNNING)

    startService("/usr/bin/k5start",
                 args="-p %s %s" % (PIDFILE, DAEMON_OPTS),
                 donotify=True)


@synchronized
def stop():
    stopService("/var/run/k5start.pid")

def status():
    return isServiceRunning("/var/run/k5start.pid")
