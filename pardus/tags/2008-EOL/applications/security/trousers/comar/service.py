from comar.service import *
import comar

serviceType = "script"
serviceDesc = _({"en": "TrouSers",
                 "tr": "TrouSers"})

tpm_modules = ("tpm", "%s" % config.get("TPM_MODULES", ""))

def load_module():
    for drv in tpm_modules:
        run("/sbin/modprobe", drv)

@synchronized
def start():
    load_module()
    startService(command="/usr/sbin/tcsd",
                 args="-f",
                 pidfile="/var/run/tcsd.pid",
                 chuid="tss",
                 makepid=True,
                 detach=True,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/tcsd.pid",
                user="tss",
                donotify=True)

def status():
    return isServiceRunning("/var/run/tcsd.pid")
