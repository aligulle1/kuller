import os
from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "fnfx Daemon",
                 "tr": "fnfx Sunucusu"})

def start():
    if 0 != run("/sbin/modprobe toshiba_acpi"):
        fail("cannot load toshiba acpi module")

    ret = run("start-stop-daemon --start --quiet --exec /usr/sbin/fnfxd --pidfile /var/run/fnfxd.pid")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --quiet --exec /usr/sbin/fnfxd")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/fnfxd.pid")
