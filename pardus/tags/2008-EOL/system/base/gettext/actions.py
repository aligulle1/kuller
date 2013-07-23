#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -Dgcc_is_lint" % get.CFLAGS())
    shelltools.export("CXXFLAGS","%s -Dgcc_is_lint" % get.CXXFLAGS())

    # Build with --without-included-gettext (will use that of glibc), as we
    # need preloadable_libintl.so for new help2man
    autotools.autoreconf("-fi")
    autotools.configure("--disable-java \
                         --disable-csharp \
                         --without-included-gettext \
                         --with-included-libcroco \
                         --with-included-glib \
                         --with-included-libxml \
                         --without-emacs \
                         --enable-nls \
                         --disable-static")

def build():
    autotools.make("GMSGFMT=../src/msgfmt")

def install():
    autotools.rawInstall("DESTDIR=%s docdir=/usr/share/doc/%s/html" % (get.installDIR(), get.srcTAG()))

    pisitools.doexe("gettext-tools/misc/gettextize", "/usr/bin")

    # Remove C# & Java stuff
    pisitools.remove("/usr/share/doc/%s/html/examples/build-aux/csharp*" % get.srcTAG())
    pisitools.remove("/usr/share/doc/%s/html/examples/build-aux/java*" % get.srcTAG())
    pisitools.removeDir("/usr/share/doc/%s/html/examples/*java*" % get.srcTAG())
    pisitools.removeDir("/usr/share/doc/%s/html/*java*" % get.srcTAG())

    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "NEWS", "THANKS", "TODO")
