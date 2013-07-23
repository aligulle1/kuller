serviceType = "local"
serviceDesc = "Tapioca"
serviceDefault = "off"

from comar.service import *

def start():
    if 0 == run('/sbin/start-stop-daemon --quiet --start --exec /usr/bin/tapioca --pidfile /var/run/tapioca.pid'):
        notify("System.Service.changed", "started")

def stop():
    if 0 == run("/sbin/start-stop-daemon --stop --pidfile /var/run/tapioca.pid"):
        notify("System.Service.changed", "stopped")

def status():
    return checkDeamon("/var/run/tapioca.pid")

