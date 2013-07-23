#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.system("xmkmf")
    shelltools.touch("doc/man/lib/tmp._man")
    shelltools.touch("doc/man/lib/tmp.man")
    autotools.make("World")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    # rename example nasd.conf.eg to nasd.conf and change it so that NAS
    # doesn't change mixer's settings (inspired by Debian package):
    pisitools.domove("/etc/nas/nasd.conf.eg", "/etc/nas/", "nasd.conf")
    pisitools.dosed("%s/etc/nas/nasd.conf" % get.installDIR(), "MixerInit\t\"yes\"", "MixerInit\t\"no\"")
