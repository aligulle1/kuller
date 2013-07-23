#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="xerces-c-src_%s" % get.srcVERSION().replace(".","_")

def setup():
    shelltools.export("XERCESCROOT","%s" % get.curDIR())
    pisitools.cd("src/xercesc")
    shelltools.system("./runConfigure -plinux -cgcc -xg++ -P/usr")

def build():
    pisitools.cd("src/xercesc")
    autotools.make()

def install():
    pisitools.cd("src/xercesc")
    autotools.rawInstall("DESTDIR=%s install" % get.installDIR())

    pisitools.cd("../..")
    pisitools.dohtml("doc/html/*", "Readme.html")
    pisitools.dodoc("KEYS", "LICENSE*", "NOTICE", "STATUS", "credits.txt")
