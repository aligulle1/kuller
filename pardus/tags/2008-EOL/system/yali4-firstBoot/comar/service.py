from comar.service import *
import os

serviceType = "script"
serviceDesc = "Yet Another Linux Installer v4"
serviceDefault = "off"

@synchronized
def start(boot=False):
    startDependencies("acpid", "hal")

    if call("zorg", "Xorg.Display", "ready", (boot,)) == 0:
        fail("Not starting as zorg returned an error")

    loadEnvironment()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    os.environ["HOME"]="/root"
    os.environ["USER"]="root"
    startService(command="/usr/bin/xinit",
                 args="/usr/bin/yali4-bin -f -- vt7 -nolisten tcp -br",
                 donotify=True,
                 detach=True)

@synchronized
def stop():
    stopService(command="/usr/bin/killall",
                args="yali4-bin",
                donotify=True)

def ready():
    if is_on() == "on":
        start(True)
