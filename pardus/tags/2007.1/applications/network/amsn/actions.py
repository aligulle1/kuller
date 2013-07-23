#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("dstdir=%s/usr/share slnkdir=%s/usr/bin" % (get.installDIR(),get.installDIR()))

    pisitools.dodir("/usr/share/pixmaps")
    shelltools.copy("icons/64x64/aMSN_64.png", "%s/usr/share/pixmaps/amsn.png" % get.installDIR())

    pisitools.dodoc("/usr/share/amsn/docs/*")
    pisitools.removeDir("/usr/share/amsn/docs")

    pisitools.removeDir("/usr/share/amsn/plugins/winflash")
    pisitools.removeDir("/usr/share/amsn/plugins/QuickTimeTcl3.1")
    pisitools.removeDir("/usr/share/amsn/plugins/applescript")
    pisitools.removeDir("/usr/share/amsn/plugins/tclCarbonNotification")
    pisitools.removeDir("/usr/share/amsn/plugins/tclAE2.0")
    pisitools.removeDir("/usr/share/amsn/utils/macosx")
    pisitools.removeDir("/usr/share/icons")

    # Default browser firefox
    pisitools.dosed("%s/usr/share/amsn/config.tcl" % get.installDIR(), "mozilla", "firefox");

    # Default file browser konqueror
    pisitools.dosed("%s/usr/share/amsn/config.tcl" % get.installDIR(), "my_filemanager open", "konqueror");
