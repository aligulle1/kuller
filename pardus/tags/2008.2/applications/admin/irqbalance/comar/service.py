from comar.service import *

serviceType = "local"
serviceConf = "irqbalance"
serviceDefault = "conditional"
serviceDesc = _({"en": "Irqbalance Daemon",
                 "tr": "Irqbalance Servisi"})

@synchronized
def start():
    startService(command="/usr/sbin/irqbalance",
                 args = config.get("args",""),
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/sbin/irqbalance",
                donotify=True)

def ready():
    import os
    status = is_on()
    if status == "on" or (status == "conditional" and os.path.exists("/sys/devices/system/cpu/cpu1")):
        start()

def status():
    return isServiceRunning(command="/usr/sbin/irqbalance")
