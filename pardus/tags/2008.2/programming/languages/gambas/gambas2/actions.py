#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-bzlib2 \
                         --enable-zlib \
                         --enable-mysql \
                         --enable-odbc \
                         --enable-postgresql \
                         --disable-sqlite2 \
                         --enable-sqlite3 \
                         --enable-firebird \
                         --enable-gtk \
                         --enable-gtksvg \
                         --enable-pdf \
                         --enable-net \
                         --enable-curl \
                         --enable-smtp \
                         --enable-pcre \
                         --enable-qt \
                         --disable-qte \
                         --enable-kde \
                         --enable-sdl \
                         --enable-sdlsound \
                         --enable-xml \
                         --enable-v4l \
                         --enable-crypt \
                         --enable-opengl \
                         --enable-corba \
                         --enable-image \
                         --enable-desktop \
                         --with-bzlib2-libraries=/lib \
                         --with-kde-includes=%s/include \
                         --with-kde-libraries=%s/lib"
                         % (get.kdeDIR(), get.kdeDIR()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s XDG_UTILS=''" % get.installDIR())
    pisitools.remove("/usr/lib/gambas2/gb.[ls][ao]")
    pisitools.remove("/usr/lib/gambas2/gb.so.*")
    pisitools.remove("/usr/share/gambas2/help/help.tar.gz")

    for mime in "main/mime/application-x-gambas", "app/mime/application-x-gambasscript":
        pisitools.insinto("/usr/share/mime/packages", "%s.xml" % mime)
        pisitools.insinto("/usr/share/icons/hicolor/64x64/mimetypes", "%s.png" % mime)

    for res in 16, 32, 48, 64, 128:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (res, res), "comp/src/gb.form/stock/default/%s/gambas.png" % res, "gambas2.png")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "ChangeLog")
