serviceType = "server"
serviceDesc = _({"en": "Apache Web Server",
                 "tr": "Apache Web Sunucusu"})
serviceConf = "apache2"

import os
from comar.service import *

def start():
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"
    ret = run("/usr/sbin/apache2ctl -d /usr/lib/apache2/ -f /etc/apache2/httpd.conf %s -k start" % config.get("APACHE2_OPTS", ""))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/usr/sbin/apache2ctl -d /usr/lib/apache2/ -f /etc/apache2/httpd.conf %s -k stop" % config.get("APACHE2_OPTS", ""))
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def reload():
    run("/usr/sbin/apache2ctl -d /usr/lib/apache2/ -f /etc/apache2/httpd.conf %s -k graceful" % config.get("APACHE2_OPTS", ""))

def status():
    return checkDaemon("/var/run/apache2.pid")
