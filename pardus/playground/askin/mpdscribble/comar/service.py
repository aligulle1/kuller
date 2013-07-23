from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Last.fm Submission Daemon",
                 "tr": "Last.fm Bildirim Sunucusu"})
serviceDefault = "off"

@synchronized
def start():
    startDependencies("mpd")
    startService(command="/usr/bin/mpdscribble",
                 pidfile="/var/run/mpdscribble.pid",
                 detach=True,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/mpdscribble.pid",
                command="/usr/bin/mpdscribble",
                donotify=True)

def status():
    return isServiceRunning(command="/usr/bin/mpdscribble", \
                            pidfile="/var/run/mpdscribble.pid")
