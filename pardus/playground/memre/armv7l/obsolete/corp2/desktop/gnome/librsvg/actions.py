#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--with-croco \
                         --disable-gnome-print \
                         --disable-mozilla-plugin \
                         --disable-static \
                         --with-gnu-ld \
                         --with-x-includes=%(SysRoot)s/usr/include/X11 \
                         --with-x-libraries=%(SysRoot)s/usr/lib" % autotools.environment)
                         # FIXME: --with-svgz

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.removeDir("/usr/lib/mozilla/plugins")
    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("COPYING", "AUTHORS", "ChangeLog", "README")
