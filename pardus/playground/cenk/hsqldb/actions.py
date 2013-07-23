#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "hsqldb"

def setup():
    # We don't need compiled jar files
    shelltools.unlinkDir("lib")

def build():
    shelltools.cd("build")
    shelltools.system("ant jar jarclient jarsqltool jarutil")

def install():
    pisitools.dosbin("bin/hsqldb")

    # Jar library files
    pisitools.insinto("/usr/share/java", "*.jar")

    # Links
    pisitools.dosym("/var/lib/hsqldb/sqltool.rc", "/etc/hsqldb/sqltool.rc")
    pisitools.dosym("/var/lib/hsqldb/server.properties", "/etc/hsqldb/server.properties")

    # Logs
    pisitools.dodir("/var/log/hsqldb")
    shelltools.touch("%s/var/log/hsqldb/hsqldb.log" % get.installDIR())

    # Pid file
    pisitools.dodir("/var/run/hsqldb")

    # Documents
    pisitools.dohtml("doc/*.html", "doc/guide/*", "doc/src/*")
    pisitools.dodoc("readme.txt", "doc/*.txt")
