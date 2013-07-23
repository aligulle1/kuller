#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

if "_" in get.srcVERSION():
    WorkDir = get.srcNAME()

def setup():
    # FIXME --with-softfloat is not proper for all ARM devices

    autotools.autoreconf("-fvi")
    autotools.configure("--with-cards=pdaudiocf \
                         --with-oss=yes \
                         --disable-dependency-tracking \
                         --with-versioned \
                         --with-libdl \
                         --with-softfloat \
                         --enable-shared \
                         --disable-aload \
                         --disable-python")
                         # FIXME --enable-python

    # rpath fix
    pisitools.dosed("libtool", "^hardcode_libdir_flag_spec=.*", "hardcode_libdir_flag_spec=\"\"")
    pisitools.dosed("libtool", "^runpath_var=LD_RUN_PATH", "runpath_var=DIE_RPATH_DIE")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ChangeLog", "TODO", "COPYING", "doc/*.txt")
