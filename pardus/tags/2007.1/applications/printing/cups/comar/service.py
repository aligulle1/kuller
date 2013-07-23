from comar.service import *
import os

serviceType = "server"
serviceDefault = "on"
serviceDesc = _({"en": "CUPS Printer Server",
                 "tr": "CUPS Yazıcı Sunucusu"})

soket = "/var/run/cups/cups.sock"

def start():
    call("System.Service.start", "hplip")
    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/cupsd")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/cupsd")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    # We can not use pid for "is cups running check", it has a habit of restarting itself
    # return checkDaemon("/var/run/cupsd.pid")

    if os.path.exists(soket):
        return True
    else:
        return False

