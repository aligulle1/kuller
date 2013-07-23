serviceType = "server"
serviceDesc = _({"en": "VLC Server",
                 "tr": "VLC Sunucusu"})
serviceDefault = "on"

from comar.service import *

pidFile = "/var/run/vlc.pid"

@synchronized
def start():
    startService(command="/usr/bin/cvlc",
                 args="--ttl 12 --quiet -I telnet --telnet-password x --telnet-port 4433 --rtsp-host 0.0.0.0:5554",
                 detach=True,
                 chuid="vlc:vlc",
                 pidfile=pidFile,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidFile,
                donotify=True)
    import os
    os.unlink(pidFile);

def status():
    return isServiceRunning(pidFile)
