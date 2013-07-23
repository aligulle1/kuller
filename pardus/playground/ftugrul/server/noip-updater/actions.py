#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="noip-%s-1" % get.srcVERSION()

def setup():
    pisitools.dosed("noip2.c", "PREFIX\"/etc", "\"/etc")

def build():
    autotools.make()

def install():
    pisitools.dosbin("noip2")

    pisitools.dodoc("COPYING", "README.*", "LEEME.PRIMERO", "LIESMICH.ERST.deutsch", "LISEZMOI.ENPREMIER")

