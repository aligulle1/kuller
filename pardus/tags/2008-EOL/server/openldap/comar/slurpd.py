from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Slurpd Daemon",
                 "tr": "Slurpd Sunucusu"})

def start():
    startService(command="/usr/libexec/slurpd",
                 donotify=True)

def stop():
    stopService(command="/usr/libexec/slurpd",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/libexec/slurpd")
