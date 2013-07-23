#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    # install locales in /usr/share/locale
    pisitools.dosed("intl/Makefile.in", "^\(localedir = \).*", "\1/usr/share/locale")
    pisitools.dosed("po/Makefile.in.in", "^\(localedir = \).*", "\1/usr/share/locale")
    pisitools.dosed("configure", '^#define LOCALEDIR.*','#define LOCALEDIR "/usr/share/locale"')

    # install the .desktop in /usr/share/applications
    pisitools.dosed("client/Makefile.in", "^\(desktopfiledir = \).*", "\1/usr/share/applications")

    autotools.configure("--disable-dependency-tracking \
                         --with-zlib \
                         --enable-nls \
                         --with-readline \
                         --enable-client=gtk-2.0")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    # We will use our desktop file, for now
    pisitools.remove("/usr/share/applications/freeciv.desktop")

    shelltools.system("./manual/civmanual")
    pisitools.dohtml("manual*.html")
    pisitools.remove("/usr/bin/civmanual")

    pisitools.dodoc("ChangeLog", "NEWS", "doc/BUGS", "doc/CodingStyle", "doc/HACKING", "doc/HOWTOPLAY", "doc/PEOPLE", "doc/README*", "doc/TODO")

