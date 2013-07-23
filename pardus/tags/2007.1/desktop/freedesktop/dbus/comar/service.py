from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "DBUS Desktop Message Bus",
                 "tr": "DBUS Masaüstü İletişim Sistemi"})
serviceDefault = "on"

def cleanup():
    try:
        os.unlink("/var/run/dbus/pid")
        os.unlink("/var/run/dbus/system_bus_socket")
    except:
        pass

def start():
    # create universally unique id
    if not os.path.exists("/var/lib/dbus/machine-id"):
        run("/usr/bin/dbus-uuidgen --ensure")

    ret = run("/sbin/start-stop-daemon --start --pidfile /var/run/dbus/pid --exec /usr/bin/dbus-daemon -- --system")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --pidfile /var/run/dbus/pid")
    if ret == 0:
        cleanup()
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def reload():
    run("dbus-send --print-reply --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig")

def status():
    return checkDaemon("/var/run/dbus/pid")
