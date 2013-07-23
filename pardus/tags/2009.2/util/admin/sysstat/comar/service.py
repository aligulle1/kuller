# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "System activity data collector",
                 "tr": "Sistem etkinliği veri toplayıcısı"})

MSG_ERR_FAILSYST = _({"en": "Sysstat failed.",
                      "tr": "Sysstat başarısız oldu.",
                      })

cron_file = '/etc/cron.d/sysstat'

def check_log():
    if not os.path.exists("/var/log/sa/sa21"):
        run("/usr/lib/sa/sadc -F -L -")

@synchronized
def start():
    check_log()
    startDependencies("vixie-cron")
    if run("/usr/lib/sa/sa1 -d 1 1") == 0:
        run("ln -sf /etc/sysstat/sysstat.cron /etc/cron.d/sysstat")
        notify("System.Service.changed", "started")
    else:
        fail(MSG_ERR_FAILSYST)

@synchronized
def stop():
    if run("rm -f /etc/cron.d/sysstat") == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail(MSG_ERR_FAILSYST)

@synchronized
def status():
    return os.access(cron_file, os.F_OK)
