from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "No-Ip updater",
                 "tr": "No-Ip güncelleyici"})

@synchronized
def start():
    startService(command="/usr/sbin/noip2",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/noip2",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/sbin/noip2") 
