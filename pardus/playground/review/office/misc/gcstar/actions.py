#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s" % get.srcNAME()

""""Missing perl-Modules:
    Gtk2::Spell
    MIME::Base64
    MP3::Info
    MP3::Tag
    Net::FreeDB
    Ogg::Vorbis::Header::PurePerl
    DateTime::Format::Strptime
    """


def install():
    shelltools.system("./install --prefix=%s/usr --noclean --nomenu --verbose" % get.installDIR())

    pisitools.insinto("/usr/share/applications", "share/applications/gcstar.desktop")
    pisitools.insinto("/usr/share/pixmaps", "share/gcstar/icons/gcstar_64x64.png", "gcstar.png")
    pisitools.insinto("/usr/share/mime/packages", "share/applications/gcstar.xml")

    for i in("16", "22", "24", "32", "36", "48", "64", "72", "96", "128", "192", "256"):
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps/" %(i,i), "share/gcstar/icons/gcstar_%sx%s.png" %(i,i), "gcstar.png")

    pisitools.dodoc("CHANGELOG", "README", "LICENSE")
