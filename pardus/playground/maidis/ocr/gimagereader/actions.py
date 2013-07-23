#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    pythonmodules.compile()

def install():
    # not works yet:
    # http://www.google.com.tr/search?hl=tr&safe=off&q=%22Not+a+TIFF+file%2C+bad+version+number%22
    pythonmodules.install()

    pisitools.removeDir("/usr/share/doc/gimagereader-%s" % get.srcVERSION())

    pisitools.dodoc("AUTHORS", "changelog", "COPYING", "README", "TODO", "src/manual.html")
