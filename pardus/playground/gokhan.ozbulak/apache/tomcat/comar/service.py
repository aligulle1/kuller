#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from comar.service import *

serviceDefault = "off"
serviceType = "server"
serviceDesc = _({"en": "Apache Tomcat Web Server",
                 "tr": "Apache Tomcat Web Sunucusu"
                 })

serviceConf = "tomcat6"

BASEDIR = "/opt/tomcat6"
PIDFILE = "/var/run/tomcat6.pid"

os.environ["LC_ALL"] = "C"
os.environ["LANG"] = "C"
os.environ["CATALINA_PID"] = PIDFILE
os.environ["JAVA_HOME"] = "/opt/sun-jdk"

def apply_conf():
    import os
    # Try shorten here later
    # server.xml
    os.system("sed -i -e '0,/<Connector port=\".*\" protocol=\"HTTP\/1.1\"/s//<Connector port=\"%s\" protocol=\"HTTP\/1.1\"/' %s/conf/server.xml" % (config.get("CONNECTOR_PORT"), BASEDIR))
    os.system("sed -i -e '0,/connectionTimeout=\".*\"/s//connectionTimeout=\"%s\"/' %s/conf/server.xml" % (config.get("CONNECTION_TIMEOUT"), BASEDIR))
    os.system("sed -i -e '0,/redirectPort=\".*\"/s//redirectPort=\"%s\"/' %s/conf/server.xml" % (config.get("CONNECTOR_REDIRECT_PORT"), BASEDIR))

    # tomcat-users.xml
    os.system("sed -i -e 's/<user username=\".*\" password=\".*\" roles=\"manager.*\"\/>/<user username=\"%s\" password=\"%s\" roles=\"%s\"\/>/' %s/conf/tomcat-users.xml" % (config.get("MANAGER_USER"), config.get("MANAGER_PWD"), config.get("MANAGER_ROLES"), BASEDIR))
    os.system("sed -i -e 's/<user username=\".*\" password=\".*\" roles=\"admin\"\/>/<user username=\"%s\" password=\"%s\" roles=\"admin\"\/>/' %s/conf/tomcat-users.xml" % (config.get("ADMIN_USER"), config.get("ADMIN_PWD"), BASEDIR))
    os.system("sed -i -e 's/<user username=\".*\" password=\".*\" roles=\"tomcat\"\/>/<user username=\"%s\" password=\"%s\" roles=\"tomcat\"\/>/' %s/conf/tomcat-users.xml" % (config.get("TOMCAT_USER"), config.get("TOMCAT_PWD"), BASEDIR))

@synchronized
def start():
    apply_conf()
    startService(command="%s/bin/startup.sh" % BASEDIR,
                 donotify=True)

@synchronized
def stop():
    stopService(command = "%s/bin/shutdown.sh" % BASEDIR,
                args = "",
                donotify = True)

def status():
    return isServiceRunning(PIDFILE)
