#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Reusable-Cluster-Components-glue--glue-1.0.9"

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--enable-fatal-warnings=yes \
                         --with-deamon-group=haclient \
                         --with-deamon-user=hacluster \
                         --without-docbook \
                         --localstatedir=/var")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

