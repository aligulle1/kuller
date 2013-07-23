from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Smartlink Modem Manager",
                 "tr": "Smartlink Modem Yöneticisi"})

def start():
    args = ""
    mod = config.get("MODULE", "alsa")

    if mod == "alsa":
        args = "--alsa %s" % config.get("HW_SLOT", "modem:1")
    else:
        os.system("/sbin/modprobe %s" % mod)
        mdev = config.get("MDEV", "")
        if mdev == "":
            mdev = "/dev/%s0" % mod

        if not os.path.exists(mdev):
            os.system("/bin/mknod %s c 242 0" % mdev)

        args = mdev

    ret = run("start-stop-daemon --start --background --nicelevel=%s --make-pidfile \
               --pidfile /var/run/slmodemd.pid --startas /usr/sbin/slmodemd \
               -- -country=%s -g=%s %s %s" % ( \
               config.get("NICE", "-6"), \
               config.get("COUNTRY", "TURKEY"), \
               config.get("GROUP", "dialout"), \
               config.get("SLMODEM_OPTS", ""), \
               args))

    if config.get("LN_DEV", "") != "":
        try:
            os.symlink(config.get("DEV", "/dev/ttySL0"), config.get("LN_DEV", "/dev/modem"))
        except:
            pass

    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("start-stop-daemon --stop --quiet --pidfile /var/run/slmodemd.pid")

    try:
        os.unlink("/var/run/slmodemd.pid")
        os.unlink(config.get("LN_DEV", "/dev/modem"))
    except:
        pass

    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/slmodemd.pid")
