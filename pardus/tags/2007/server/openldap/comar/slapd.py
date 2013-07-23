import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Slapd Daemon",
                 "tr": "Slapd Sunucusu"})

def start():
    ret = run("start-stop-daemon --start --quiet --pidfile /var/run/openldap/slapd.pid --exec /usr/libexec/slapd -u ldap -g ldap")
    if ret == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("start-stop-daemon --stop --signal 2 --quiet --pidfile /var/run/openldap/slapd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")

def status():
    return checkDaemon("/var/run/openldap/slapd.pid")
