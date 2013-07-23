from comar.service import *

serviceType = "script"
serviceConf = "bluetooth"
serviceDefault = "conditional"
serviceDesc = _({"en": "Bluetooth Utils",
                 "tr": "Bluetooth Araçları"})

@synchronized
def start():
    for daemon in ["HCID", "RFCOMM", "HID2HCI"]:
        if config.get("%s_ENABLE" % daemon) == "true":
            # Start the hcid daemon, rfcomm and hid2hci utilities.
            startService(command=config.get("%s_DAEMON" % daemon),
                         args=config.get("%s_OPTIONS" % daemon),
                         donotify=True)


@synchronized
def stop():
    # Stop the hcid daemon
    stopService(command=config.get("HCID_DAEMON"),
                donotify=True)

def ready():
    import os
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/class/bluetooth/")):
        start()

def status():
    return isServiceRunning(command=config.get("HCID_DAEMON"))
