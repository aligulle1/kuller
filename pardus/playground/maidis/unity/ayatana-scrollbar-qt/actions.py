#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt4
from pisi.actionsapi import get

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    pisitools.dolib_so("liboverlay-scrollbar-qt.so.1.0.0")
    pisitools.dosym("/usr/lib/liboverlay-scrollbar-qt.so.1.0.0", "/usr/lib/liboverlay-scrollbar-qt.so.1.0")
    pisitools.dosym("/usr/lib/liboverlay-scrollbar-qt.so.1.0.0", "/usr/lib/liboverlay-scrollbar-qt.so.1")
    pisitools.dosym("/usr/lib/liboverlay-scrollbar-qt.so.1.0.0", "/usr/lib/liboverlay-scrollbar-qt.so")

    pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README", "TODO")
