#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "MuSE-%s" % get.srcVERSION()
docsdir = "%s/%s" % (get.docDIR(), get.srcTAG())

def setup():
    autotools.configure()

def build():
    autotools.make('CXXFLAGS="%s -fpermissive" \
                    CFLAGS="%s"' % (get.CXXFLAGS(), get.CFLAGS()))

def install():
    autotools.rawInstall("DESTDIR=%s docsdir=%s" % (get.installDIR(), docsdir))

    pisitools.doman("doc/muse.1")
    pisitools.dodoc("COPYING", "KNOWN-BUGS", "USAGE", "AUTHORS", "TODO", "ChangeLog", "NEWS", "README")
