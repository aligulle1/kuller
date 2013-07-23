serviceType = "server"
serviceDesc = _({"en": "SMB Network Sharing",
                 "tr": "SMB Ağ Paylaşımı"})

from comar.service import *

def start():
    ret = 0
    for d in ["smbd", "nmbd"]:
        ret += run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/%s -- -D" % d)

    if config.get("winbind", "no") == "yes":
        ret += run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/winbindd")

    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = 0
    for d in ["smbd", "nmbd"]:
        ret += run("/sbin/start-stop-daemon --stop --quiet --pidfile /var/run/samba/%s.pid" % d)

    if config.get("winbind", "no") == "yes":
        ret += run("/sbin/start-stop-daemon --stop --quiet --oknodo --pidfile /var/run/samba/winbindd.pid")

    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def reload():
    for d in ["smbd", "nmbd", "winbindd"]:
        run("/usr/bin/killall -HUP %s" % d)

def status():
    return checkDaemon("/var/run/samba/smbd.pid")
