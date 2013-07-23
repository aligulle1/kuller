from comar.service import *

serviceType = "script"
serviceConf = "bluetooth"
serviceDefault = "conditional"
serviceDesc = _({"en": "Bluetooth Utils",
                 "tr": "Bluetooth Araçları"})

@synchronized
def start():
    for daemon in ["HCID", "RFCOMM", "PAND", "DUND", "HID2HCI"]:
        if config.get("%s_ENABLE" % daemon) == "true":
            startService(command=config.get("%s_DAEMON" % daemon),
                         args=config.get("%s_OPTIONS" % daemon),
                         makepid=True,
                         pidfile="/var/run/%s.pid" % daemon.lower(),
                         donotify=True)


@synchronized
def stop():
    for daemon in ["HCID", "RFCOMM", "PAND", "DUND", "HID2HCI"]:
        if config.get("%s_ENABLE" % daemon) == "true":
            stopService(command=config.get("%s_DAEMON" % daemon),
                        pidfile="/var/run/%s.pid" % daemon.lower(),
                        donotify=True)

def ready():
    import os
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/class/bluetooth/")):
        start()

def status():
    return isServiceRunning("/var/run/hcid.pid")
