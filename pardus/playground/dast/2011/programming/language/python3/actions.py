#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

#WorkDir = "Python-%s" % get.srcVERSION()
WorkDir = "Python-3.2rc3"
PythonVersion = "3.2"

def setup():
    #shelltools.export("OPT", "%s -fPIC -fwrapv" % get.CFLAGS())
    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --enable-loadable-sqlite-extensions \
                         --with-system-expat \
                         --with-system-ffi \
                         --with-signal-module \
                         --with-threads \
                         --with-pymalloc \
                         --with-libc='' \
                         --with-wide-unicode")

def build():
    autotools.make()

def check():
    autotools.make("test")
    # 5 tests failed: test_argparse test_httpservers test_import test_pydoc test_site

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/bin/2to3")
    pisitools.dodoc("LICENSE", "README")
