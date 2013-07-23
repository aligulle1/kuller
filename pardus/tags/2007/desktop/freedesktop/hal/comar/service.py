from comar.service import *
import os
import time
import socket

serviceType = "local"
serviceDesc = _({"en": "Hardware Abstraction Layer",
                 "tr": "Donanım Soyutlama Katmanı (HAL)"})
serviceDefault = "on"

def start():
    call("System.Service.start", "acpid")
    call("System.Service.start", "PolicyKit")
    call("System.Service.start", "dbus")

    waitBus("/var/run/dbus/system_bus_socket")

    ret = run("/sbin/start-stop-daemon --start -q --exec /usr/sbin/hald -- --daemon=yes --use-syslog")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop -q --pidfile /var/run/hald.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/hald.pid")
