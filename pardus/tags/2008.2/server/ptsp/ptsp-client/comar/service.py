from comar.service import *
import os
import ConfigParser

serviceType = "script"
serviceDesc = "ptsp_client"
serviceDefault = "on"
configFile = "/etc/pts-client.conf"

def configure():
    if run("/usr/bin/zorg --probe") != 0:
        fail("Not starting as zorg returned an error")

def has_thin():
    return "thin" in open("/proc/cmdline", "r").read()

def get_xserver():
    if not os.path.exists(configFile):
        fail("%s file does not exist" % configFile)

    cp = ConfigParser.ConfigParser()
    cp.read(configFile)

    try:
        return cp.get("Server", "xserver")
    except ConfigParser.NoOptionError:
        fail("XSERVER not defined in %s" % configFile)

def start_pulse():
    if run("/usr/bin/pulseaudio --system -D") != 0:
        fail("not starting pulseaudio")

def start():
    if not has_thin():
        fail("Not thin setup.")

    startDependencies("acpid")
    configure()
    loadEnvironment()
    os.environ["XAUTHLOCALHOSTNAME"]=os.uname()[1]
    os.environ["HOME"]="/root"
    os.environ["USER"]="root"
    start_pulse()

    while True:
        run("X -query %s vt7 -br" % get_xserver())

def stop():
    if not has_thin():
        fail("Not thin setup.")

    if 0 == run("/usr/bin/killall X"):
        notify("System.Service.changed", "stopped")
