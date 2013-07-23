# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Internet Key Exchange (IKE) Daemon",
                 "tr": "İnternet Anahtar Değişim (IKE) Servisi"})

serviceConf = "racoon"

@synchronized
def start():
    startService(command="/usr/sbin/racoon",
                 args="-f %s %s" % (config.get("RACOON_CONF", ""), config.get("RACOON_OPTS", "")),
                 pidfile="/var/run/racoon.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/racoon",
                pidfile="/var/run/racoon.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/racoon.pid")
