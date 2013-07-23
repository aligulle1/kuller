import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Dovecot POP3/IMAP Server",
                 "tr": "Dovecot POP3/IMAP Sunucusu"})

def start():
    ret = run("start-stop-daemon --start --exec /usr/sbin/dovecot --pidfile /var/run/dovecot/master.pid")
    if ret == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("start-stop-daemon --stop --exec /usr/sbin/dovecot --pidfile /var/run/dovecot/master.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")

def status():
    return checkDaemon("/var/run/dovecot/master.pid")
