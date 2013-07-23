import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Tomcat Servlet Container",
                 "tr": "Tomcat Servlet Sunucusu"})
serviceConf = "tomcat5"

def start():
    reply = run("/usr/bin/jsvc \
                -Djava.endorsed.dirs=/usr/share/tomcat5/common/endorsed \
                -Dcatalina.home=/usr/share/tomcat5 \
                -Dcatalina.base=/var/lib/tomcat5 \
                -cp /usr/share/tomcat5/bin/bootstrap.jar \
                -outfile /var/lib/tomcat5/logs/catalina.out \
                -errfile /var/lib/tomcat5/logs/catalina.err \
                -pidfile /var/run/tomcat5/jsvc.pid \
                -home /opt/sun-jre \
                -user tomcat \
                -jvm server \
                org.apache.catalina.startup.Bootstrap")

    if reply == 0:
        notify("System.Service.changed", "started")
    else:
        fail(reply.stderr)

def stop():
    reply = run("/usr/bin/jsvc \
                 -stop \
                 -pidfile /var/run/tomcat5/jsvc.pid \
                 org.apache.catalina.startup.Bootstrap")

    if reply == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail(reply.stderr)

def status():
    return checkDaemon("/var/run/tomcat5/jsvc.pid")
