#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

BASEDIR = "/opt/tomcat6/"

def setup():
    pass

def install():
    pisitools.dodir(BASEDIR)
    pisitools.insinto(BASEDIR, "./*")

    pisitools.dodoc("LICENSE", "NOTICE", "RELEASE-NOTES")
    for f in ("LICENSE", "NOTICE", "RELEASE-NOTES"):
        pisitools.remove("%s%s" % (BASEDIR, f))

    # Reach the log files from standard log dir /var/log
    pisitools.dosym("/opt/tomcat6/logs", "/var/log/tomcat6")
