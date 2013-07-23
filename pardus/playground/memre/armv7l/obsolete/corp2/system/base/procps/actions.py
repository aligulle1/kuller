#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    crosstools.make('CC="%(CC)s" \
                     CFLAGS="%(CFLAGS)s" \
                     LDFLAGS="%(LDFLAGS)s" \
                     CURSES=-lncurses \
                     lib64=lib \
                     m64=' % crosstools.environment)

def install():
    crosstools.rawInstall('ln_f="ln -sf" \
                           ldconfig="true" \
                           lib64=lib \
                           DESTDIR=%s \
                           SKIP="/bin/kill \
                           /usr/share/man/man1/kill.1"' % get.installDIR())

    pisitools.dosym("libproc-%s.so" % get.srcVERSION(), "/lib/libproc.so")

    pisitools.dodoc("BUGS", "NEWS", "TODO", "ps/HACKING")
