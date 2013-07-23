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

def status():
    return checkDaemon("/var/run/kdm.pid")

def start():
    lock = FileLock("/var/run/comar-kdebase.lock")
    lock.lock()
    if status():
        return
    configure()
    call("System.Service.start", "acpid")
    call("System.Service.start", "hal")
    loadEnvironment()
    setLang()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    ret = run("/sbin/start-stop-daemon", "--start", "--quiet", "--exe", "/usr/kde/3.5/bin/kdm")
    if ret == 0:
        notify("System.Service.changed", "started")
    lock.unlock()

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --exe /usr/kde/3.5/bin/kdm")
    if ret == 0:
        notify("System.Service.changed", "stopped")
