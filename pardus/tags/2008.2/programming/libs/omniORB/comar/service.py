import os
import socket
from comar.service import *

serviceType = "server"
serviceDefault = "off"

serviceDesc = _({"en": "CORBA Naming Service",
                 "tr": "CORBA İsimlendirme Servisi"})
serviceConf = "omniNames"

logDir = "/var/log/omniNames"
keyFile = "/var/lib/omniMapper/NameService"

def start():
    options = "-errlog %s/error.log -logdir %s" % (logDir, logDir)
    hostname = socket.gethostname()
    tcpPort = config.get("TCPPORT", "2809")

    if not os.path.exists(logDir + "/omninames-%s.log" % hostname):
        options += " -start %s" % tcpPort

    #FIXME: -u omni is needed?
    ret = startService(command="/usr/bin/omniNames",
            args=options,
            pidfile="/var/run/omniNames.pid",
            makepid=True,
            detach=True)

    if ret == 0:
        ret = run("/bin/sh", "-c",
                "/usr/bin/genior IDL:omg.org/CosNaming/NamingContextExt:1.0 %s %s NameService > %s"
                % (hostname, tcpPort, keyFile))

        if ret == 0:
            notify("System.Service", "Changed", (script(), "started"))
        else:
            fail("Unable to configure NameService with genior")
    else:
        err = "Unable to start service"
        if ret.stderr != "":
            err = "Unable to start: %s" % str(ret.stderr)
        fail(err)

def stop():
    ret = stopService(pidfile="/var/run/omniNames.pid", donotify=True)

    if os.access(keyFile, os.F_OK):
        os.unlink(keyFile)

def status():
    return isServiceRunning("/var/run/omniNames.pid")
