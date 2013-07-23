from comar.service import *
import os

serviceType = "script"
serviceDesc = "Yet Another Linux Installer"
serviceDefault = "on"

def configure():
    if run("/sbin/zorg --boot") != 0:
        fail("Not starting as zorg returned an error")

def has_livecd():
    if "livecd" in open("/proc/cmdline", "r").read() or "livedisk" in open("/proc/cmdline", "r").read():
        return True
    return False

def start():
    if not has_livecd():
        fail("Not in CD root.")

    call("System.Service.start", "acpid")
    configure()
    loadEnvironment()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    os.environ["HOME"]="/root"
    os.environ["USER"]="root"
    # if 0 == run("/usr/bin/xinit /usr/bin/yali-bin -- tty6 vt7 -nolisten tcp -br"):
    if 0 == run("/usr/bin/xinit /usr/bin/yali-bin -- vt7 -nolisten tcp -br"):
        notify("System.Service.changed", "started")

def stop():
    if not has_livecd():
        fail("Not in CD root.")

    if 0 == run("/usr/bin/killall yali-bin"):
        notify("System.Service.changed", "stopped")
