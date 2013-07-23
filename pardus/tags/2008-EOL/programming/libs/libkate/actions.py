#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("configure", "HAVE_PYTHON=yes", "HAVE_PYTHON=no")
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/share/doc/libkate")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcTAG()), "examples")

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "THANKS")
