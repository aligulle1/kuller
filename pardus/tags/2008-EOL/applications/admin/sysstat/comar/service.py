from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "System activity data collector",
                 "tr": "Sistem aktive verileri toplayıcısı"})

cron_file = '/etc/cron.d/sysstat'

def check_log():
    if not os.path.exists("/var/log/sa/sa21"):
        run("/usr/lib/sa/sadc -F -L -")

def start():
    check_log()
    call("System.Service.start", "vixie-cron")
    if run("/usr/lib/sa/sa1 -d 1 1") == 0:
        run("ln -fs /etc/sysstat/sysstat.cron /etc/cron.d/sysstat")
        notify("System.Service.changed", "started")
    else:
        fail("sysstat failed!")

def stop():
    if run("rm -f /etc/cron.d/sysstat") == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("sysstat failed!")

def status():
    return os.access(cron_file, os.F_OK)
