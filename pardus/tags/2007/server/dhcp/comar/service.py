import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "DHCP Daemon",
                 "tr": "DHCP Sunucusu"})

def start():
    ret = run("/sbin/start-stop-daemon --start --exec /usr/sbin/dhcpd \
               --p /var/run/dhcp/dhcpd.pid -u dhcp -g dhcp \
               -- %s %s" % (config.get("DHCPD_IFACE", ""), config.get("DHCPD_OPTS", "")))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --exec /usr/sbin/dhcpd --p /var/run/dhcp/dhcpd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/dhcp/dhcpd.pid")
