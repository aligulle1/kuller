from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "InfraRed Device Manager",
                 "tr": "Kızılötesi Aygıt Yöneticisi"})
serviceConf = "irda"

def start():
    if config.get("IRDA", "") != "yes" or config.get("IRDADEV", "") == "":
        fail("IRDA configuration not set")
    else:
        args = ""
        if config.has_key("DONGLE"):
            args += "-d %s" % config["DONGLE"]
        if config.get("DISCOVER") == "yes":
            args += " -s"
        ret = run("start-stop-daemon --start --quiet --exec /usr/sbin/irattach -- %s %s" % (config["IRDADEV"], args))
        if ret == 0:
            notify("System.Service.changed", "started")
        else:
            fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --quiet --pidfile /var/run/irattach.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/irattach.pid")
