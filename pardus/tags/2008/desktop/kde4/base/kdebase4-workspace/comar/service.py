from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "KDE4 Desktop Environment",
    "tr": "KDE4 Masaüstü Ortamı",
})
serviceDefault = "on"

def setLang():
    kdmrc_path = "/usr/kde/4/share/config/kdm/kdmrc"
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
def start(boot=False):
    if status():
        return

    if call("zorg", "Xorg.Display", "ready", (boot,)) == 0:
        fail("Not starting as zorg returned an error")

    startDependencies("acpid", "hal")
    loadEnvironment()
    setLang()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    startService(command="/usr/kde/4/bin/kdm",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/kde/4/bin/kdm",
                donotify=True)

def status():
    return isServiceRunning("/var/run/kdm.pid")

def ready():
    if is_on() == "on":
        start(boot=True)
