from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "DBUS Desktop Message Bus",
                 "tr": "DBUS Masaüstü İletişim Sistemi"})
serviceDefault = "on"

@synchronized
def start():
    # create universally unique id
    if not os.path.exists("/var/lib/dbus/machine-id"):
        run("/usr/bin/dbus-uuidgen --ensure")
    
    startService(command="/usr/bin/dbus-daemon",
                 args="--system",
                 pidfile="/var/run/dbus/pid",
                 donotify=True)

    # Extra check, ensure dbus is up and running!
    waitBus("/var/run/dbus/system_bus_socket")

@synchronized
def stop():
    reply = stopService(pidfile="/var/run/dbus/pid",
                        donotify=True)
    try:
        os.unlink("/var/run/dbus/pid")
        os.unlink("/var/run/dbus/system_bus_socket")
    except:
        pass

def reload():
    run("dbus-send --print-reply --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig")

def status():
    return isServiceRunning("/var/run/dbus/pid")
