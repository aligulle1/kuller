from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "SVN Server",
                 "tr": "SVN Sunucusu"})
serviceConf = "svnserve"

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --background --make-pidfile \
               --pidfile /var/run/svnserve.pid --exec /usr/bin/svnserve \
               --chuid %s:%s -- --foreground --daemon %s" % (config.get("SVNSERVE_USER", "apache"),
                                                             config.get("SVNSERVE_GROUP", "apache"),
                                                             config.get("SVNSERVE_OPTS", "--root=/var/svn")))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile /var/run/svnserve.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/svnserve.pid")
