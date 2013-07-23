from comar.service import *

serviceType = "script"
serviceConf = "bluetooth"
serviceDefault = "conditional"
serviceDesc = _({"en": "Bluetooth Service",
                 "tr": "Bluetooth Hizmeti"})

@synchronized
def start():
    # Start bluetoothd
    startDependencies("hal")
    startService(command="/usr/sbin/bluetoothd", donotify=True)

    if config.get("RFCOMM_ENABLE") == "true":
        startService(command=config.get("RFCOMM_DAEMON"),
                     args=config.get("RFCOMM_OPTIONS"),
                     donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/bluetoothd", donotify=True)

def ready():
    import os
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/class/bluetooth/")):
        start()

def status():
    return isServiceRunning(command="/usr/sbin/bluetoothd")
