#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="tools-20070815"

def build():
    autotools.make ('LIB_DIR=/usr/lib/uml CC=%s CFLAGS="%s \
                    -DTUNTAP -D_FILE_OFFSET_BITS=64 -D_LARGEFILE64_SOURCE" \
                     all' % (get.CC(), get.CFLAGS()))

def install():
    autotools.rawInstall ("DESTDIR=%s LIB_DIR=/usr/lib/uml" % get.installDIR())

    #pisitools.dodoc("README", "LICENSE")
