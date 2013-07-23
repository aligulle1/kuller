# -*- coding: utf-8 -*-
from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "fnfx Daemon",
                 "tr": "fnfx Servisi"})

MSG_ERR_LOADTOSHACPI = _({"en": "Couldn't load Toshiba ACPI module.",
                          "tr": "Toshiba ACPI modülü yüklenemedi.",
                          })

@synchronized
def start():
    if not os.path.exists("/proc/acpi/toshiba/keys"):
        reply = run("/sbin/modprobe -s toshiba_acpi")
        if reply != 0:
            fail(MSG_ERR_LOADTOSHACPI)

    startService(command="/usr/sbin/fnfxd",
                 pidfile="/var/run/fnfxd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/fnfxd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/fnfxd.pid")
