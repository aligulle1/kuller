#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LC_ALL", "C")
    crosstools.prepare()

    shelltools.chmod("configure", 0755)
    shelltools.chmod("cnf/*", 0755)
    shelltools.chmod("Makefile*", 0755)
    shelltools.system('./configure \
                       --target=arm \
                       --sysroot=%(RootDir)s \
                       --prefix=/usr' % crosstools.environment)

def build():
    shelltools.export("LC_ALL", "C")
    crosstools.prepare()

    shelltools.system("make")

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr")
    pisitools.domove("%(RootDir)s/usr" % crosstools.environment, "/")
    pisitools.removeDir("%(RootDir)s" % crosstools.environment)

    pisitools.remove("/usr/bin/perl")
    pisitools.remove("/usr/bin/config_data")

    pisitools.removeDir("/usr/share/man/man3/")
