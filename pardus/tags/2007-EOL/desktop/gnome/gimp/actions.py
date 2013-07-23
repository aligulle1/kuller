#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-x \
                         --disable-gtk-doc \
                         --disable-default-binary \
                         --enable-print \
                         --enable-python \
                         --without-gtkhtml2 \
                         --without-gnomeprint \
                         --with-gimpprint \
                         --with-libjpeg \
                         --with-libexif \
                         --with-png \
                         --with-librsvg \
                         --with-lcms \
                         --with-poppler \
                         --with-tiff \
                         --with-aa")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("gimp-remote-2.4", "/usr/bin/gimp-remote")
    pisitools.dosym("gimp-console-2.4", "/usr/bin/gimp-console")
    pisitools.dosym("gimp-2.4", "/usr/bin/gimp")

    pythonmodules.fixCompiledPy("/usr/lib/gimp/2.0/")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "HACKING", "NEWS", "README*")
