#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

def setup():
    perlmodules.configure("MP_TRACE=1 \
                           MP_DEBUG=1 \
                           MP_USE_DSO=1 \
                           MP_APXS=/usr/sbin/apxs2")

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodir("/var/www/localhost/cgi-perl")
