#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir = "/%s/%s" % (get.docDIR(), get.srcTAG())

def setup():
    autotools.configure("--disable-static \
                         --enable-digests \
                         --enable-storages \
                         --enable-assertions \
                         --enable-assert-messages \
                         --disable-gtk-doc \
                         --with-xml-parser=expat \
                         --with-raptor=system \
                         --with-rasqal=system \
                         --with-openssl-digests \
                         --with-html-dir=%s" % docdir)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("%s/html" % docdir, "%s/%s/redland/*" % (get.installDIR(), docdir))
    pisitools.removeDir("%s/redland" % docdir)
    pisitools.dohtml("*.html")
    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "NEWS", "README")
