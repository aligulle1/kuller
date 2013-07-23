#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CFLAGS",'%s -DVERSION=\\"%s\\" -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE' % (get.CFLAGS(),get.srcVERSION()))
    autotools.make("CC=%s" % get.CC())

def install():
    autotools.make('PREFIX="%s/usr" \
                    SBINDIR="%s/usr/sbin" \
                    MANDIR="%s/usr/share/man" \
                    install' % (get.installDIR(), get.installDIR(), get.installDIR()))

    pisitools.dodoc('AUTHORS', 'README', 'tmpwatch.cron.example')
