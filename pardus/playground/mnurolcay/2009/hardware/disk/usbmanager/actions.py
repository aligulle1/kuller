#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir="usbmanager"

def build():
    pythonmodules.compile()

def install():

    shelltools.unlink("locale/*.mo")
    for i in ("ar", "de", "es", "fr", "nl", "pt_BR", "ru", "th", "tr"):
        pisitools.domo("locale/%s.po" %i, "%s" %i, "%s.mo" % i)

    pythonmodules.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
