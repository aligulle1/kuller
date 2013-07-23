from comar.service import *
import os

serviceType = "local"
serviceDesc = _({"en": "Zemberek Spell Checker",
                 "tr": "Zemberek Yazım Denetimi"})

def start():
    loadEnvironment()

    if not os.environ.has_key("JAVA_HOME"):
        fail("Where is Java?")
    javapath = os.environ["JAVA_HOME"]

    os.environ["LC_ALL"] = "tr_TR.UTF-8"
    os.chdir("/opt/zemberek-server")

    ret = run("/sbin/start-stop-daemon -b --start --quiet --pidfile \
               /var/run/zemberek.pid --make-pidfile --exec %s/bin/java \
               -- -jar -Xverify:none -Xms12m -Xmx14m /opt/zemberek-server/zemberek_server-0.6.jar" % javapath)
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon", "--stop", "--quiet", "--pidfile", "/var/run/zemberek.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def ready():
    loadEnvironment()

    s = get_profile("System.Service.setState")
    if s:
        state = s["state"]
        if state == "on":
            start()
    else:
        if os.environ["LC_ALL"] == "tr_TR.UTF-8":
            start()

def status():
    return checkDaemon("/var/run/zemberek.pid")
