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

    autotools.autoreconf("-fi")

    # Static libs should be enabled for mono compiler
    autotools.configure("--enable-parallel-mark \
                         --with-profile4=yes \
                         --with-tls=pthread \
                         --with-jit=yes")

# Not ready parameters
# --with-monotouch=yes \

def build():
    shelltools.export("MONO_SHARED_DIR", get.curDIR())

    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING.LIB", "ChangeLog", "LICENSE", "NEWS", "README")
