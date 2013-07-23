#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.touch("README")

    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-gnutls \
                         --enable-openssl \
                         --enable-cypher \
                         --enable-signature \
                         --disable-coverage \
                         --enable-old-eet-file-format \
                         ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
