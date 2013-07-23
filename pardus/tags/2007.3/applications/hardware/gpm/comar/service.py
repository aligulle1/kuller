serviceType = "local"
serviceDesc = _({"en": "Console Mouse Daemon",
                 "tr": "Konsol için Fare Sunucusu"})

from comar.service import *

def start():
    args = ""
    # gpm cares for the order of args
    if config.has_key("RESPONSIVENESS"):
        args += "-r %s " % config.get("RESPONSIVENESS")
    if config.has_key("REPEAT_TYPE"):
        args += "-R%s " % config.get("REPEAT_TYPE")

    args += config.get("APPEND", "")
    ret = run ("start-stop-daemon --start --quiet --exec /usr/sbin/gpm \
                -- -m %s -t %s %s" % (config.get("MOUSEDEV", "/dev/input/mice"), \
                                      config.get("MOUSE", "imps2"), \
                                      args))

    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --quiet --pidfile /var/run/gpm.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/gpm.pid")
