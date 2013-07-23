from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "System Message Logger",
                 "tr": "Sistem Mesajları Kütüğü"})
serviceDefault = "on"

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --background --exec /usr/sbin/syslogd -- -m 15")

    waitBus("/dev/log", stream=False)
    ret += run("/sbin/start-stop-daemon --start --quiet --background --exec /usr/sbin/klogd -- -c 3 -2")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --oknodo --retry 15 --quiet --pidfile /var/run/klogd.pid")
    ret += run("/sbin/start-stop-daemon --stop --oknodo --retry 15 --quiet --pidfile /var/run/syslogd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/syslogd.pid")
