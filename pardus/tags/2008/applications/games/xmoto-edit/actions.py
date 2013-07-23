#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-rpath \
                         --with-enable-www=1 \
                         --with-enable-zoom=1 \
                         --enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # Strange handling of man
    #shelltools.system("gunzip xmoto-edit.6.gz")

    # man does not work, removing for now
    pisitools.removeDir("/usr/share/man")
    #pisitools.doman("xmoto-edit.6")

