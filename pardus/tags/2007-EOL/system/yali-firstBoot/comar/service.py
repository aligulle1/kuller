from comar.service import *
import os

serviceType = "script"
serviceDesc = "Yet Another Linux Installer - OEM Install"
serviceDefault = "on"

def start(boot=False):
    call("System.Service.start", "acpid")
    call("System.Service.stop", "kdebase")

    if not boot and run("/sbin/zorg") != 0:
        fail("Not starting as zorg returned an error")

    loadEnvironment()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    os.environ["HOME"]="/root"
    os.environ["USER"]="root"
    if 0 == run("/usr/bin/xinit /usr/bin/yali-bin -- vt7 -nolisten tcp -br"):
        notify("System.Service.changed", "started")

def stop():
    if 0 == run("/usr/bin/killall yali-bin"):
        notify("System.Service.changed", "stopped")

def ready():
    if is_on() == "on":
        if run("/sbin/zorg --boot") != 0:
            fail("Not starting as zorg returned an error")

        start(boot=True)
