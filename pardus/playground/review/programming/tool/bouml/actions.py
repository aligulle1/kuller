#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

if get.ARCH() == "x86_64":
    shelltools.export("QMAKESPEC", "linux-g++-64")
else:
    shelltools.export("QMAKESPEC", "linux-g++-32")


def build():
    autotools.make("DESTDIR=%s" % get.installDIR())


def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())
    pisitools.dosed("%s/usr/share/applications/bouml.desktop" \
            % get.installDIR(), "%s" % get.installDIR(), "")
    pisitools.dosed("%s/usr/share/applications/projectControl.desktop" \
            % get.installDIR(), "%s" % get.installDIR(), "")
    pisitools.dosed("%s/usr/share/applications/projectSynchro.desktop" \
            % get.installDIR(), "%s" % get.installDIR(), "")
