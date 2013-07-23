#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-static=no \
                         --includedir=/usr/include/libpisock \
                         --with-java=no \
                         --with-perl=yes \
                         --with-python=yes \
                         --with-libpng=/usr \
                         --with-readline=yes")

def build():
    autotools.make()
    #FIXME
    #for [source]/bindings/Perl,
    #perl-module_src_prep
    #perl-module_src_compile


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    perlmodules.fixLocalPod()
    pythonmodules.fixCompiledPy()

    pisitools.dodoc("ChangeLog", "README", "doc/README*", "doc/TODO", "NEWS", "AUTHORS")
