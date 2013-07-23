#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--sysconfdir=/etc/icecast \
                         --disable-static \
                         --enable-yp")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Create Log Dir
    pisitools.dodir("/var/log/icecast")
    pisitools.dodir("/var/run/icecast")

    #Correct permissions
    shelltools.chmod("%s/var/log/icecast" % get.installDIR(), 0755 )
    shelltools.chmod("%s/etc/icecast/icecast.xml" % get.installDIR(),  0640)
    shelltools.chmod("%s/var/run/icecast" % get.installDIR(), 0755)

    pisitools.insinto("/usr/share/pixmaps","web/icecast.png")

    pisitools.doman("debian/icecast2.1")
    pisitools.dohtml("doc/*.html")
    pisitools.dohtml("doc/*.css")
    pisitools.dohtml("doc/*.jpg")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README","TODO","HACKING")

    pisitools.removeDir("/usr/share/doc/icecast")
