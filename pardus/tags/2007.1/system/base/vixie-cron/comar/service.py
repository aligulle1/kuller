from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Cron Task Scheduler",
                 "tr": "Cron Görev Zamanlayıcı"})

def start():
    ret = run("start-stop-daemon --start --quiet --exec /usr/sbin/cron")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --quiet --pidfile /var/run/cron.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/cron.pid")
