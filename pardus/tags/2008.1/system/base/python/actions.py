#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("OPT", "%s -fPIC -fwrapv" % get.CFLAGS())
    autotools.configure("--with-fpectl \
                         --enable-shared \
                         --enable-ipv6 \
                         --with-threads \
                         --with-libc='' \
                         --enable-unicode=ucs4 \
                         --with-wctype-functions")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "altinstall")

    pisitools.dosym("/usr/bin/python2.5","/usr/bin/python")
    pisitools.dosym("/usr/bin/python2.5-config","/usr/bin/python-config")
    pisitools.dosym("/usr/lib/python2.5/pdb.py","/usr/bin/pdb")

    # FIXME: caglar10ur
    pisitools.remove("/usr/bin/idle")
    pisitools.removeDir("/usr/lib/python2.5/idlelib")
    pisitools.remove("/usr/lib/python2.5/lib-dynload/_tkinter.so")
    pisitools.removeDir("/usr/lib/python2.5/lib-tk")

    pisitools.dodoc("LICENSE", "README")
