serviceType = "local"
serviceDesc = _({"en": "HP Printer/Scanner Services",
                 "tr": "HP Yazıcı/Tarayıcı Servisleri"})
serviceDefault = "on"

from comar.service import *

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/hpiod")
    ret += run("/sbin/start-stop-daemon --quiet --start --exec /usr/share/hplip/hpssd.py --pidfile /var/run/hpssd.pid")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet -n hpiod")
    ret += run("/sbin/start-stop-daemon --stop --pidfile /var/run/hpssd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to start service")

def status():
    return checkDaemon("/var/run/hpssd.pid")
