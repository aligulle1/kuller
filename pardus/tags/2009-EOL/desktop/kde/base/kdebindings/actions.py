#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    shelltools.export("HOME", get.workDIR())
    shelltools.makedirs("build")
    shelltools.cd("build")
    #Since Mono cs compiler raises sandbox violation we disable CS bindings for now
    cmaketools.configure("-DBUILD_csharp=OFF -DENABLE_KROSSFALCON=ON -DENABLE_PHP-QT=ON -DENABLE_SMOKE=ON -DRUBY_SITE_LIB_DIR=/usr/lib/ruby/site_ruby/1.8 -DRUBY_SITE_ARCH_DIR=/usr/lib/ruby/site_ruby/1.8/i686-linux", installPrefix="/usr/kde/4", sourceDir="..")

def build():
    shelltools.export("HOME", get.workDIR())
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.export("HOME", get.workDIR())
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #shelltools.chmod("%s/usr/kde/4/share/apps/pykde4/pykdeuic4.py" % get.installDIR(), 0755)

    # pykde4uic symlink
    pisitools.dosym("/usr/lib/%s/site-packages/PyQt4/uic/pykdeuic4.py" % get.curPYTHON(), "/usr/kde/4/bin/pykde4uic")

    pisitools.dosym("/usr/kde/4/bin/rbqtapi", "/usr/kde/4/bin/rbqt4api")
    pisitools.dosym("/usr/kde/4/bin/rbqtapi", "/usr/kde/4/bin/rbkdeapi")
    pisitools.dosym("/usr/kde/4/bin/rbqtapi", "/usr/kde/4/bin/rbkde4api")
    #pisitools.dosym("/usr/kde/4/bin/rbqtapi", "/usr/kde/4/bin/rbplasmaapi")
