from comar.service import *
import os

serviceType = "script"
serviceDesc = "Yet Another Linux Installer v4"
serviceDefault = "on"

def has_livecd():
    if "livecd" in open("/proc/cmdline", "r").read() or "livedisk" in open("/proc/cmdline", "r").read() or os.path.exists("/etc/yali-is-firstboot"):
        return True
    return False

@synchronized
def start(boot=False):
    if not has_livecd():
        fail("Not in CD root.")

    startDependencies("acpid", "hal")

    if call("zorg", "Xorg.Display", "ready", (boot,)) == 0:
        fail("Not starting as zorg returned an error")

    loadEnvironment()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    os.environ["HOME"]="/root"
    os.environ["USER"]="root"
    startService(command="/usr/bin/xinit",
                 args="/usr/bin/yali4-bin -- vt7 -nolisten tcp -br",
                 donotify=True,
                 detach=True)

@synchronized
def stop():
    if not has_livecd():
        fail("Not in CD root.")
    stopService(command="/usr/bin/killall",
                args="yali4-bin",
                donotify=True)

def ready():
    if is_on() == "on":
        start(True)
