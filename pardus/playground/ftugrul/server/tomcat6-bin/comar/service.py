serviceType = "server"
serviceDesc = _({"en": "Tomcat6 server",
                 "tr": "Tomcat6 sunucusu"})
serviceConf = "tomcat6-bin"

from comar.service import *

@synchronized
def start():

    loadEnvironment()

    if not os.environ.has_key("JAVA_HOME"):
        fail("JAVA_HOME is not set")

    javapath = os.environ["JAVA_HOME"]
    args = []
    args.append("-Djava.util.logging.manager=%s" % config.get("JAVA_OPTS", ""))
    args.append("-Djava.util.logging.config.file=%s" % config.get("LOGGING_CONFIG", ""))
    args.append("-classpath %s%s" % (javapath, config.get("CLASSPATH", "")))
    args.append("-Dcatalina.base=%s" % config.get("CATALINA_BASE", ""))
    args.append("-Dcatalina.home=%s" % config.get("CATALINA_HOME", ""))
    args.append("-Djava.io.tmpdir=%s" % config.get("CATALINA_TMPDIR", ""))
    args.append("org.apache.catalina.startup.Bootstrap start")
    startService(command="%s/bin/java" % javapath,
                 args=" ".join(args),
                 pidfile="/var/run/tomcat6-bin.pid",
                 makepid=True,
                 detach=True,
                 donotify=True)

@synchronized
def stop():

    loadEnvironment()

    if not os.environ.has_key("JAVA_HOME"):
        fail("JAVA_HOME is not set")

    javapath = os.environ["JAVA_HOME"]
    args = []
    args.append("-Djava.util.logging.manager=%s" % config.get("JAVA_OPTS", ""))
    args.append("-classpath %s" % config.get("CLASSPATH", ""))
    args.append("-Dcatalina.base=%s" % config.get("CATALINA_BASE", ""))
    args.append("-Dcatalina.home=%s" % config.get("CATALINA_HOME", ""))
    args.append("-Djava.io.tmpdir=%s" % config.get("CATALINA_TMPDIR", ""))
    args.append("org.apache.catalina.startup.Bootstrap stop")

    stopService(command="%s/bin/java" % javapath,
                 args=" ".join(args),
                 donotify=True)

def status():
    return isServiceRunning("/var/run/tomcat6-bin.pid")
