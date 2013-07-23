#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "spring_0.76b1"

def setup():
    scons.make("configure \
                optimize=2 \
                prefix=/usr \
                installprefix=%s/usr \
                datadir=share/spring \
                bindir=bin \
                libdir=lib/spring \
                strip=0" % get.installDIR())

def build():
    scons.make()

def install():
    scons.install()

    pisitools.dohtml("*.html", "Documentation/userdocs/'*.html'", "Documentation/*.html")
    pisitools.insinto("/usr/share/doc/%s/Lobby" % get.srcTAG(), "Documentation/Lobby")
    pisitools.insinto("/usr/share/doc/%s/UML" % get.srcTAG(), "Documentation/UML/*")
    pisitools.dodoc("Documentation/*.txt", "Documentation/*.odt")
