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
    crosstools.configure("--with-zlib \
                          --with-python \
                          --with-readline \
                          --enable-ipv6 \
                          --disable-static")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    for i in ["", "-python"]:
        pisitools.rename("/%s/libxml2%s-%s" % (get.docDIR(), i, get.srcVERSION()), "libxml2%s" % i)

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
    pisitools.removeDir("/usr/share/gtk-doc")
