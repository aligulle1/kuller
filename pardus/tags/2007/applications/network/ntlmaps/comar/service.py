from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "NTLM Proxy Daemon",
                 "tr": "NTLM Vekil Sunucusu"})

pidfile = "/var/run/ntlmaps.pid"

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --background --chuid ntlmaps --make-pidfile --pidfile %s --exec /usr/bin/python -- /usr/bin/ntlmaps" % pidfile)
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile %s" % pidfile)
    if ret == 0:
        os.remove(pidfile)
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon(pidfile)
