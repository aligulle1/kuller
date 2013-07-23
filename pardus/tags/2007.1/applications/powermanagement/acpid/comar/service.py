from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "ACPI Daemon",
                 "tr": "ACPI Sunucusu"})
serviceDefault = "on"

def check_config():
    if not os.path.exists("/proc/acpi"):
        fail("ACPI support has not been found")

def start():
    check_config()

    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/acpid -- -c /etc/acpi/events")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/acpid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def reload():
    run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/acpid --signal HUP")
