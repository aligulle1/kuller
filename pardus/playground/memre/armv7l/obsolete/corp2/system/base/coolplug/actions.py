#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools

WorkDir = "coolplug"

def build():
    crosstools.make('CC="%(CC)s" \
                     CFLAGS="%(CFLAGS)s" \
                     LDFLAGS="%(LDFLAGS)s" \
                     STRIP=%(STRIP)s' % crosstools.environment)

def install():
    pisitools.dosbin("coolplug", "/sbin")
