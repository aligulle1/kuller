#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    scons.make("mode=release-symbols \
                enable-shared-portaudio=no enable-shared-webcam=no \
                enable-shared-wengocurl=no enable-shared-phapi=no \
                softphone-runtime softphone")

def install():
    scons.install("prefix=%s/usr mode=release-symbols softphone-install" % get.installDIR())
    pisitools.dosed("%s/usr/bin/wengophone" % get.installDIR(), get.installDIR(), "")
    shelltools.chmod("%s/usr/bin/wengophone" % get.installDIR())
    pisitools.insinto("/usr/share/pixmaps", "wengophone.png")
    pisitools.insinto("/usr/share/applications", "wengophone.desktop")
    pisitools.dodoc("COPYING", "TODO", "README*")
