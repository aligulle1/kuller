#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "gtk+-%s" % get.srcVERSION()

def setup():
    cache = [ "ac_cv_lib_jpeg_jpeg_destroy_decompress=yes",
              "ac_cv_lib_jpeg_jpeg_simple_progression=yes",
              "LIBJPEG='-ljpeg'",
              "gio_can_sniff=yes" ]

    autotools.autoreconf("-fvi")
    autotools.configure("--with-libjpeg \
                         --with-libtiff \
                         --with-libjasper\
                         --with-libpng \
                         --with-gdktarget=x11 \
                         --enable-xinerama \
                         --with-xinput=yes \
                         --enable-xkb \
                         --enable-shm \
                         --disable-introspection \
                         --with-included-loaders=png \
                         --disable-glibtest \
                         --x-includes=%(SysRoot)s/usr/include/X11 \
                         --x-libraries=%(SysRoot)s/usr/lib \
                         --with-gnu-ld \
                         --disable-cups \
                         " % autotools.environment, cache=cache)
                         # FIXME: --disable-cups will be fixed.
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # remove empty dir
    pisitools.removeDir("/usr/share/man")
    pisitools.dodoc("AUTHORS", "README*", "HACKING", "ChangeLog*", "NEWS*")
