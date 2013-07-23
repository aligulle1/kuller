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
from pisi.actionsapi import pythonmodules

WorkDir="kdebase-workspace-%s" % get.srcVERSION().split("_")[0]

def setup():
    # PAM files are named kde4.pam and kde4-np.pam. We should change cmake file to make PAM modules work
    pisitools.dosed("ConfigureChecks.cmake", "KDE4_COMMON_PAM_SERVICE \"kde\"", "KDE4_COMMON_PAM_SERVICE \"kde4\"")

    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DKDE_HOME_DEFAULT=.kde4", installPrefix="/usr/kde/4",sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")

    #do not use existing system KDM while creating the new one
    shelltools.export("GENKDMCONF_FLAGS", "--no-old")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Put kdmrc into /etc/X11/kdm, so it can be modified on live CDs
    pisitools.domove("usr/kde/4/share/config/kdm/kdmrc", "/etc/X11/kdm/", "kdmrc4")
    pisitools.dosym("/etc/X11/kdm/kdmrc4", "usr/kde/4/share/config/kdm/kdmrc")

    #remove pyc files
    pythonmodules.fixCompiledPy("/usr/lib/%s/site-packages/PyKDE4" % get.curPYTHON())
    pythonmodules.fixCompiledPy("/usr/kde/4/share/apps/plasma_scriptengine_python")
