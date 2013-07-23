#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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

    # configure for sdl-client
    autotools.configure("--disable-dependency-tracking \
                         --with-zlib \
                         --without-esd \
                         --enable-nls \
                         --with-readline \
                         --enable-client=sdl")

def build():
    # compile sdl gui
    autotools.make()

    # backup sdl gui
    pisitools.dosed("client/freeciv.desktop", "civclient", "civclient-sdl")
    shelltools.move("client/freeciv.desktop", "client/freeciv-sdl.desktop")
    shelltools.system("echo GenericName=Freeciv-SDL>>client/freeciv-sdl.desktop")
    shelltools.move("client/civclient", "client/civclient-sdl")

    # I need to configure twice to enable both sdl and gtk guis
    autotools.configure("--disable-dependency-tracking \
                         --with-zlib \
                         --without-esd \
                         --enable-nls \
                         --with-readline \
                         --enable-client=gtk-2.0")
    #compile gtk gui
    autotools.make()

def install():
    # gtk gui
    pisitools.dosed("client/freeciv.desktop", "civclient", "civclient-gtk")
    shelltools.system("echo GenericName=Freeciv-GTK>>client/freeciv.desktop")
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())
    pisitools.rename("/usr/bin/civclient", "civclient-gtk")

    # sdl gui
    pisitools.insinto("/usr/bin", "client/civclient-sdl", "civclient-sdl")
    pisitools.insinto("/usr/share/applications", "client/freeciv-sdl.desktop", "freeciv-sdl.desktop")
    pisitools.insinto("/usr/share/freeciv/themes/gui-sdl", "data/themes/gui-sdl/human")

    # cleanup
    pisitools.remove("/usr/share/freeciv/themes/gui-sdl/human/Makefile*")

    # docs
    shelltools.system("./manual/civmanual")
    pisitools.dohtml("manual*.html")

    pisitools.dodoc("ChangeLog", "NEWS", "doc/BUGS", "doc/CodingStyle", "doc/HACKING", "doc/HOWTOPLAY", "doc/PEOPLE", "doc/README*", "doc/TODO")
