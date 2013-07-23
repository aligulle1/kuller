#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure("--with-xine \
                   --with-libgpod \
                   --with-opengl \
                   --with-mp4v2 \
                   --with-libnjb \
                   --with-libmtp \
                   --without-gstreamer \
                   --without-xmms \
                   --disable-debug")

def build():
    kde.make()

def install():
    kde.install()

    # Let KsCD handle Audio CDs
    pisitools.remove("/usr/kde/3.5/share/apps/konqueror/servicemenus/amarok_play_audiocd.desktop")

    # Let lastfm handle last.fm links
    pisitools.remove("/usr/kde/3.5/share/services/amaroklastfm.protocol")

