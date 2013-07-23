#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-alsa \
                         --with-jack \
                         --with-oss")

def build():
    autotools.make()

def install():
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dolib("src/libstk.so.4.4.3")
    pisitools.dosym("/usr/lib/libstk.so.4.4.3", "/usr/lib/libstk.so.4")
    pisitools.dosym("/usr/lib/libstk.so.4", "/usr/lib/libstk.so")

    pisitools.insinto("/usr/include/stk", "include/*.h")
    pisitools.insinto("/usr/include/stk", "include/*.msg")
    pisitools.insinto("/usr/include/stk", "include/*.tbl")

    pisitools.insinto("/usr/share/stk/rawwaves", "rawwaves/*.raw")

    pisitools.dodoc("README", "doc/*.txt")

    pisitools.dohtml("doc/*.html", "doc/html/*")
