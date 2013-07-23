from comar.service import *
import os

serviceType="server"
serviceDesc = _({"en": "MySQL Database Server",
                 "tr": "MySQL Veritabanı Sunucusu"})

def check_mysql():
    if not os.path.exists("/var/lib/mysql"):
        fail("MySQL is not installed")

def start():
    check_mysql()
    ret = run("/sbin/start-stop-daemon --start --quiet --background --exec /usr/sbin/mysqld")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --retry 5 --quiet --pidfile=/var/run/mysqld/mysqld.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/mysqld/mysqld.pid")
