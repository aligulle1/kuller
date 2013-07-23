serviceType = "local"
serviceDesc = _({"en": "ifplugd Daemon",
                 "tr": "ifplugd Sunucusu"})

from comar.service import *


def isWireless(if_name):
    from pardus import netutils
    ifc = netutils.IF(if_name)
    if ifc.isWireless():
        return True

@synchronized
def start():
    for if_name in config.get("INTERFACES").split(","):
        if isWireless(if_name):
            startService(command="/usr/sbin/ifplugd",
                         args="%s -i %s" %(config.get("IFPLUGD_WLAN_ARGS", ""), if_name),
                         donotify=True)
        else:
            startService(command="/usr/sbin/ifplugd",
                         args="%s -i %s" %(config.get("IFPLUGD_ARGS", ""), if_name),
                         pidfile="/var/run/ifplugd.%s.pid" % if_name)

@synchronized
def stop():
    for if_name in config.get("INTERFACES").split(","):
        stopService(pidfile="/var/run/ifplugd.%s.pid" % if_name,
                    donotify=True)

def status():
    for if_name in config.get("INTERFACES").split(","):
        if not isServiceRunning("/var/run/ifplugd.%s.pid" % if_name):
            return False
        return True

