from comar.service import *

serviceType = "local"
serviceDefault = "off"
serviceDesc = _({"en": "InfraRed Controller Manager",
                 "tr": "InfraRed Bağlantı Yöneticisi"})

def start():
    ret = 0
    ret += run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/lircd -- %s" % config.get("LIRCD_OPTS", ""))

    if config.get("USE_LIRCMD", "no") == "yes":
        ret += run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/lircmd")

    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = 0
    ret += run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/lircd")

    if config.get("USE_LIRCMD", "no") == "yes":
        ret += run("/sbin/start-stop-daemon --stop --quiet --exec /usr/sbin/lircmd")

    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/lircd.pid")
