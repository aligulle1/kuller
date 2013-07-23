#!/usr/bin/python

from comar.service import *

serviceType="server"
serviceDesc = _({"en": "x2goserver Server",
                 "tr": "x2goserver Sunucusu"})

@synchronized
def start():

    #setup the environment
    os.environ["PATH"] = "/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/sbin:/usr/local/bin"
    # start the service
    startService(command="/usr/sbin/x2gocleansessions",
                 makepid=True,
                 pidfile="/var/run/x2goserver.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/x2goserver.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/x2goserver.pid")
