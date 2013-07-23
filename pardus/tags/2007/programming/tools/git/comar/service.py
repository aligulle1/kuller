from comar.service import *
import os

serviceType = "local"
serviceDesc = "Git"
serviceDefault = "off"

def start():
    try:
        options = os.env["GITDAEMON_OPTS"]
    except:
        options = ""
    ret = run("/sbin/start-stop-daemon --start -q --background --exec /usr/bin/git-daemon -- %s" % options)
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop -q --exec /usr/bin/git-daemon")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
