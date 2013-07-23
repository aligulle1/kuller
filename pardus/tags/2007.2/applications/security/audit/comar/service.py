from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "AUDIT Daemon",
                 "tr": "AUDIT DNS Sunucusu"})

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --exec /sbin/auditd")
    if ret == 0:
        # load rules
        run("/sbin/auditctl -R /etc/audit/audit.rules")
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --exec /sbin/auditd -- stop")
    if ret == 0:
        # clean rules
        run("/sbin/auditctl -D")
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/auditd.pid")
