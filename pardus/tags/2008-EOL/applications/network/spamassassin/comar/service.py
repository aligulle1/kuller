from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Spam detection daemon",
                 "tr": "Spam filtreleme servisi"})

serviceConf = "spamd"
pidfile="/var/run/spamd.pid"

@synchronized
def start():
    startService(command="/usr/bin/spamd",
                 args="-d -r %s %s %s" % (pidfile, config.get("PARAMS",""), config.get("EXTRA","")),
                 nice = int(config.get("NICELEVEL","-0")),
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile,
                donotify=True)

def status():
    return isServiceRunning(pidfile)
