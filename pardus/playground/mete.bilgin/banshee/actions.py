#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-docs \
                         --disable-gnome \
                         --disable-torrent \
                         --enable-schemas-install \
                         --enable-gapless-playback \
                         --disable-karma \
                         --enable-shared \
                         --enable-user-help \
                         --disable-youtube \
                         --disable-appledevice \
                         --disable-ipod \
                         --enable-tests \
                         --with-vendor-build-id=\"Pardus Linux\" \
                         --enable-boo \
                         --disable-gio \
                         --disable-gio-hardware \
                         --disable-moonlight \
                         --enable-mtp \
                         --enable-daap \
                         --enable-remote-audio \
                         --enable-podcast \
                         --enable-release \
                         --disable-shave  ")

                        #--disable-clutter \
                        #
def build():
    autotools.make()

def install():
    shelltools.export("MONO_SHARED_DIR", "/usr/lib/mono/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    #pisitools.dosed("%s/usr/lib/pkgconfig/*.pc" % get.installDIR(), '/usr/lib/', '/usr/lib/banshee')
    pisitools.move("%s/%s/*" % (get.installDIR(), get.installDIR()), "%s/usr/lib/banshee/" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
    pisitools.removeDir("/var")
