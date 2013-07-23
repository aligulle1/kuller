#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.remove("/usr/share/doc/ipython/README_Windows.txt")
    pisitools.rename("/usr/share/doc/ipython", get.srcTAG())

    pisitools.domove("/usr/share/doc/%s/ipython.el"% get.srcTAG(), "/usr/share/emacs/site-lisp/")
