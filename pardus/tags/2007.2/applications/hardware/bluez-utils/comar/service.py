from comar.service import *

serviceType = "script"
serviceConf = "bluetooth"
serviceDesc = _({"en": "Bluetooth Utils",
                 "tr": "Bluetooth Araçları"})

@synchronized
def start():
    for daemon in ["HCID", "RFCOMM", "PAND", "DUND", "HID2HCI"]:
        if config.get("%s_ENABLE" % daemon) == "true":
            startService(command=config.get("%s_DAEMON" % daemon), args=config.get("%s_OPTIONS" % daemon), donotify=True)


@synchronized
def stop():
    for daemon in ["HCID", "RFCOMM", "PAND", "DUND", "HID2HCI"]:
        if config.get("%s_ENABLE" % daemon) == "true":
            stopService(command=config.get("%s_DAEMON" % daemon), donotify=True)

def ready():
    import os
    status = get_profile("System.Service.setState")
    if status:
        state = status["state"]
        if state == "on":
            start()
    else:
        if os.path.exists("/sys/class/bluetooth/"):
            start()
