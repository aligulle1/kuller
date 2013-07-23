from comar.service import *

serviceType="server"
serviceDesc = _({"en": "Festival Text-to-Speech Engine",
                 "tr": "Festival Metinden Sese Dönüştürme Motoru"})

@synchronized
def start():
    startService(command="/usr/bin/festival",
                 args="--server -b /etc/festival/server.scm",
                 pidfile="/var/run/festival/festival.pid",
                 chuid="festival",
                 makepid=True,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/festival/festival.pid",
                donotify=True)

    try:
        os.unlink("/var/run/festival/festival.pid")
    except:
        pass

def status():
    return isServiceRunning("/var/run/festival/festival.pid")
