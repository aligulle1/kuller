#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # for old toolchain include order bug
    # http://sourceware.org/ml/libc-hacker/2005-09/msg00016.html
    shelltools.export("CFLAGS", "%s -std=c99" % get.CFLAGS())

    autotools.configure("-with-init-script=none \
                        --with-qemud-pid-file=/var/run/libvirt_qemud.pid \
                        --with-remote-file=/var/run/libvirtd.pid \
                        --localstatedir=/var \
                        --with-xen-proxy=yes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "NEWS", "README*", "RELNOTES", "THANKS")
