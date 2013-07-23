#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="kdebase-workspace-%s" % get.srcVERSION().split("_")[0]

def setup():
    # PAM files are named kde4.pam and kde4-np.pam. We should change cmake file to make PAM modules work
    pisitools.dosed("ConfigureChecks.cmake", "KDE4_COMMON_PAM_SERVICE \"kde\"", "KDE4_COMMON_PAM_SERVICE \"kde4\"")

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DCMAKE_BUILD_TYPE=release -DKDE_HOME_DEFAULT=.kde4", installPrefix="/usr/kde/4",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall('GENKDMCONF_FLAGS="--no-old" DESTDIR=%s' % get.installDIR())

    # Put kdmrc into /etc/X11/kdm, so it can be modified on live CDs
    pisitools.domove("usr/kde/4/share/config/kdm/kdmrc", "/etc/X11/kdm/", "kdmrc4")
    pisitools.dosym("/etc/X11/kdm/kdmrc4", "usr/kde/4/share/config/kdm/kdmrc")
