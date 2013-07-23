from comar.service import *

serviceType = "server"
serviceDesc = "Xinetd"
serviceDefault = "off"

def start():
    ret = run("/usr/sbin/xinetd -pidfile /var/run/xinetd.pid -stayalive -reuse")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --pidfile /var/run/xinetd.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def reload():
    run("/usr/bin/killall -HUP xinetd") 

def status():
    return checkDaemon("/var/run/xinetd.pid")
