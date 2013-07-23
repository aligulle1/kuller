#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    # needed by networkstatus.patch
    kde.make("-f admin/Makefile.common")

    #fix conflicting headers (connections_manager.h)
    pisitools.dosed("konversation/src/Makefile.in", 'DEFAULT_INCLUDES = -I\.@am__isrc@', "DEFAULT_INCLUDES = ")
    kde.configure("--disable-final")

def build():
    kde.make()

def install():
    kde.install()
