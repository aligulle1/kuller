from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "WPA Daemon",
                 "tr": "WPA Sunucusu"})

pidfile = "/var/run/wpa_supplicant.pid"

def start():
    try:
        opts = "-wuB -P%s %s" % (pidfile, config["OPTS"])
    except:
        fail("Failed to read configuration file")
    ret = run("/sbin/start-stop-daemon --start --quiet --pidfile %s --exec /usr/sbin/wpa_supplicant -- %s" % (pidfile, opts))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile %s --exec /usr/sbin/wpa_supplicant" % pidfile)
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon(pidfile)
