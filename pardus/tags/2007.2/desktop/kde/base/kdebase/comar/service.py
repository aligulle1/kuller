from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "KDE Desktop Environment",
    "tr": "KDE Masaüstü Ortamı",
})
serviceDefault = "on"

def configure():
    if run("/sbin/zorg --boot") != 0:
        fail("Not starting as zorg returned an error")

def setLang():
    kdmrc_path = "/etc/X11/kdm/kdmrc"
    lang = file("/etc/mudur/language").read().rstrip("\n")
    data = file(kdmrc_path).read().split("\n")
    for line in data:
        if line.startswith("#Language=") or line.startswith("Language="):
            oldlang = line.split("=")[1]
            if oldlang != lang:
                f = file(kdmrc_path, "w")
                for line in data:
                    if line.startswith("#Language=") or line.startswith("Language="):
                        f.write("Language=%s\n" % lang)
                    else:
                        f.write(line+"\n")
            break

@synchronized
def start():
    if status():
        return
    configure()
    call("System.Service.start", "acpid")
    call("System.Service.start", "hal")
    loadEnvironment()
    setLang()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    startService(command="/usr/kde/3.5/bin/kdm",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/kde/3.5/bin/kdm",
                donotify=True)

def status():
    return isServiceRunning("/var/run/kdm.pid")
