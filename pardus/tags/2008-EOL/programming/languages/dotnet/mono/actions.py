#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.chmod("%s/%s/configure" % (get.workDIR(), get.srcDIR()), 0755)

    # Static libs should be enabled for mono compiler
    autotools.configure("--enable-parallel-mark \
                         --with-static-mono=yes \
                         --with-moonlight=yes \
                         --with-glib=system \
                         --with-gc=included \
                         --with-ikvm-native=yes \
                         --with-tls=__thread \
                         --with-jit=yes \
                         --with-xen_opt=yes \
                         --with-sigaltstack=no \
                         --with-preview=yes \
                         --with-libgdiplus=installed")

def build():
    # This is required for sandbox.
    shelltools.export("MONO_SHARED_DIR", get.curDIR())

    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "NEWS", "README")
