#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir = "pychess-0.10rc1"
# ERROR: Could not load the rsvg module.
# You need to install the rsvg package which is called python-rsvg in
# Debian/Ubuntu and gnome-python2-rsvg in RPM based distributions like Fedora

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
    pisitools.dodoc("AUTHORS", "LICENSE", "README", "TRANSLATORS")
