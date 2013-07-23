#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="compiz-%s" % get.srcVERSION()

shelltools.export("HOME", get.workDIR())

def setup():
    autotools.configure("--disable-static \
                         --enable-glib \
                         --disable-gconf \
                         --disable-schemas-install \
                         --enable-dbus \
                         --enable-inotify \
                         --enable-fuse \
                         --enable-annotate \
                         --enable-librsvg \
                         --enable-gtk \
                         --enable-metacity \
                         --disable-gnome \
                         --disable-gnome-keybindings \
                         --disable-kde \
                         --enable-kconfig \
                         --enable-kde4 \
                         --with-default-plugins=core,png,decoration,wobbly,fade,minimize,cube,rotate,zoom,scale,move,resize,place,switcher,screenshot,dbus")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")
