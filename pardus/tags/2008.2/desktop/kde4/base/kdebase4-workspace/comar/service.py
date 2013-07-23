from comar.service import *
import os

serviceType = "local"
serviceDesc = _({
    "en": "KDE4 Desktop Environment",
    "tr": "KDE4 Masaüstü Ortamı",
})
serviceDefault = "off"

pidFile = "/var/run/kdm-kde4.pid"

def setLang():
    kdmrc_path = "/usr/kde/4/share/config/kdm/kdmrc"
    lang = file("/etc/mudur/language").read().rstrip("\n")

    import ConfigParser
    kdmrc = ConfigParser.ConfigParser()
    kdmrc.optionxform = str
    kdmrc.readfp(open(kdmrc_path))
    kdmrc.set('X-*-Greeter', 'Language', lang)
    kdmrc.write(open(kdmrc_path, 'wb'))

@synchronized
def start(boot=False):
    if status():
        return

    if call("zorg", "Xorg.Display", "ready", (boot,), 5 * 60) == 0:
        fail("Not starting as zorg returned an error")

    startDependencies("acpid", "hal")
    loadEnvironment()
    setLang()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    startService(command="/usr/kde/4/bin/kdm",
                 pidfile=pidFile,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidFile, donotify=True)

    #Remove pid file
    if os.access(pidFile, os.F_OK):
        os.unlink(pidFile)

def status():
    return isServiceRunning(pidFile)

def ready():
    if is_on() == "on":
        start(boot=True)
