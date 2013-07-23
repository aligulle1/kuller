from comar.service import *

import os

serviceType = "script"
serviceConf = "alsa-utils"
serviceDefault = "on"
serviceDesc = _({"en": "ALSA Utilites",
                 "tr": "ALSA Araçları"})

@synchronized
def start():
    if os.path.exists("/etc/asound.state"):
        # Get the card indexes from /proc/asound/cards
        if os.path.exists("/proc/asound/cards"):
            cards = []
            open("/proc/asound/cards", "rb").read().split("[", 1)[0].strip()


@synchronized
def stop():

def status():
    return isServiceRunning("/var/run/hcid.pid")
