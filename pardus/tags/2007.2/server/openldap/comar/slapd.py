from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "OpenLDAP Server",
                 "tr": "OpenLDAP Sunucusu"})

def start():
    startService(command="/usr/libexec/slapd",
                 args="-u ldap -g ldap",
                 pidfile="/var/run/openldap/slapd.pid",
                 donotify=True)

def stop():
    stopService(pidfile="/var/run/openldap/slapd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/openldap/slapd.pid")
