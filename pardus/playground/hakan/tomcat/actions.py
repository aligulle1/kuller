#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="apache-tomcat-%s-src" % get.srcVERSION()

def ant(path):
    cd(path)
    shelltools.system("ant")

def cd(path):
    shelltools.cd("%s/apache-tomcat-%s-src/%s" % (get.workDIR(), get.srcVERSION(), path))

def setup():
    shelltools.export("LC_ALL", "C")

    # compile jasper compiler
    writeProperties("jasper")
    ant("jasper")

    writeProperties("./")
    writeProperties("build")

    # compile jni
    ant("connectors/jni")

    # compile remaining
    ant(".")

def install():
    shelltools.cd("build/build")

    pisitools.dodir("/usr/share/tomcat5/common/endorsed")
    pisitools.dodir("/usr/share/tomcat5/server/classes")
    pisitools.dodir("/var/lib/tomcat5/shared/classes")
    pisitools.dodir("/var/lib/tomcat5/shared/lib")
    pisitools.dodir("/var/tmp/tomcat5")
    pisitools.dodir("/var/run/tomcat5")
    pisitools.dodir("/var/log/tomcat5")

    for files in ["*.jar","*.sh","*.xml"]:
        pisitools.insinto("/usr/share/tomcat5/bin", "bin/%s" % files)

    for files in ["jasper-compiler","jasper-runtime","naming-factory","naming-resources"]:
        pisitools.insinto("/usr/share/tomcat5/common/lib", "common/lib/%s.jar" % files)

    for config in ["catalina.*","context.xml","logging.properties","server*.xml","tomcat-users.xml","web.xml"]:
        pisitools.insinto("/etc/tomcat5/", "conf/%s" % config)

    for files in ["catalina-ant-jmx","catalina-ant","catalina-cluster","catalina-optional","catalina-storeconfig",
                  "catalina","servlets-default","servlets-invoker","servlets-webdav","tomcat-ajp",
                  "tomcat-apr","tomcat-coyote","tomcat-http","tomcat-jkstatus-ant"]:
        pisitools.insinto("/usr/share/tomcat5/server/lib", "server/lib/%s.jar" % files)

    # Should be renamed by user/system admin to enable CGI or SSI support.
    # CGI and SSI (server side includes) should be enabled when Tomcat is used as an standalone HTTP server, 
    # and those features are required. By default those should be supplied by the HTTP Server (Apache in 
    # this case) itself.
    pisitools.insinto("/usr/share/tomcat5/server/lib", "server/lib/servlets-cgi.renametojar")
    pisitools.insinto("/usr/share/tomcat5/server/lib", "server/lib/servlets-ssi.renametojar")

    pisitools.insinto("/usr/share/tomcat5/server/lib", "../../connectors/util/tomcat-util.jar")

    pisitools.insinto("/usr/share/tomcat5/common/i18n", "common/i18n/*.jar")
    pisitools.insinto("/etc/tomcat5/Catalina/localhost", "conf/Catalina/localhost/*manager.xml")

    pisitools.insinto("/usr/share/tomcat5/server/webapps/host-manager", "server/webapps/host-manager/*")
    pisitools.insinto("/usr/share/tomcat5/server/webapps/manager", "server/webapps/manager/*")

    pisitools.insinto("/var/lib/tomcat5/webapps/ROOT", "webapps/ROOT/*")
    pisitools.insinto("/var/lib/tomcat5/webapps/balancer", "webapps/balancer/*")
    pisitools.insinto("/var/lib/tomcat5/webapps/tomcat-docs", "webapps/tomcat-docs/*")
    pisitools.insinto("/var/lib/tomcat5/webapps/webdav", "webapps/webdav/*")

    # Symlinks
    pisitools.dosym("/etc/tomcat5/",     "/var/lib/tomcat5/conf")
    pisitools.dosym("/var/log/tomcat5/", "/var/lib/tomcat5/logs")
    pisitools.dosym("/var/tmp/tomcat5/", "/var/lib/tomcat5/temp")
    pisitools.dosym("/var/run/tomcat5/", "/var/lib/tomcat5/work")

    pisitools.dosym("/usr/share/java/commons-el.jar", "/usr/share/tomcat5/common/lib/commons-el.jar")

    # TODO:jasper-compiler-jdt.jar
    pisitools.dosym("/usr/share/java/jsp-api.jar", "/usr/share/tomcat5/common/lib/jsp-api.jar")
    # TODO: naming-factory-dbcp.jar
    pisitools.dosym("/usr/share/java/servlet-api.jar", "/usr/share/tomcat5/common/lib/servlet-api.jar")
    pisitools.dosym("/usr/share/java/commons-modeler.jar", "/usr/share/tomcat5/server/lib/commons-modeler.jar")

    # home for tomcat user
    pisitools.dosym("/var/lib/tomcat5/", "/var/lib/tomcat")

def writeProperties(relPath):
    basePath = "%s/apache-tomcat-%s-src" % (get.workDIR(), get.srcVERSION())
    path = "%s/%s" % (basePath, relPath)
    pisitools.echo("/dev/tty", path)
    pisitools.echo("%s/build.properties" % path, "compile.source=1.5")
    pisitools.echo("%s/build.properties" % path, "activation.jar=/usr/share/java/activation.jar")
    pisitools.echo("%s/build.properties" % path, "ant.jar=/usr/share/ant-tasks/lib/ant.jar")
    pisitools.echo("%s/build.properties" % path, "commons-beanutils.jar=/usr/share/java/commons-beanutils.jar")
    pisitools.echo("%s/build.properties" % path, "commons-collections.jar=/usr/share/java/commons-collections.jar")
    pisitools.echo("%s/build.properties" % path, "commons-digester.jar=/usr/share/java/commons-digester.jar")
    pisitools.echo("%s/build.properties" % path, "commons-fileupload.jar=/usr/share/java/commons-fileupload.jar")
    pisitools.echo("%s/build.properties" % path, "commons-launcher.jar=/usr/share/java/commons-launcher.jar")
    pisitools.echo("%s/build.properties" % path, "commons-logging.jar=/usr/share/java/commons-logging.jar")
    pisitools.echo("%s/build.properties" % path, "commons-logging-api.jar=/usr/share/java/commons-logging-api.jar")
    pisitools.echo("%s/build.properties" % path, "commons-modeler.jar=/usr/share/java/commons-modeler.jar")
    pisitools.echo("%s/build.properties" % path, "commons-el.jar=/usr/share/java/commons-el.jar")
    pisitools.echo("%s/build.properties" % path, "commons-daemon.jar=/usr/share/java/commons-daemon.jar")
    pisitools.echo("%s/build.properties" % path, "mail.jar=/usr/share/java/mail.jar")
    pisitools.echo("%s/build.properties" % path, "servlet-api.jar=/usr/share/java/servlet-api.jar")
    pisitools.echo("%s/build.properties" % path, "jsp-api.jar=/usr/share/java/jsp-api.jar")
    pisitools.echo("%s/build.properties" % path, "jtc.home=%s/connectors" % (basePath))
    pisitools.echo("%s/build.properties" % path, "tomcat-jni.jar=%s/connectors/jni/dist/tomcat-native.jar" % (basePath))
    pisitools.echo("%s/build.properties" % path, "tomcat-util.jar=%s/connectors/util/tomcat-util.jar" % (basePath))
    pisitools.echo("%s/build.properties" % path, "tomcat-http11.jar=%s/connectors/http11/tomcat-http11.jar" % (basePath))
