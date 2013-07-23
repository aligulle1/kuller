#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import get

def build():
    crosstools.make('CC="%(CC)s -fPIC" \
                     OPT="%(CFLAGS)s" \
                     STRIP="" \
                     SHARED="yes" \
                     PREFIX="/usr" \
                     IDSDIR="/usr/share/misc" \
                     MANDIR="/usr/share/man" \
                     all' % crosstools.environment)

def install():
    crosstools.rawInstall('DESTDIR="%s" \
                           STRIP="" \
                           SHARED="yes" \
                           PREFIX="/usr" \
                           IDSDIR="/usr/share/misc" \
                           MANDIR="/usr/share/man" \
                           install-lib' % get.installDIR())

