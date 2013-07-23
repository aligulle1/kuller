#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DENABLE_DEMO=ON -DDISABLE_ASPELL=ON -DDISABLE_TRIGGER=ON", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make("-j1")

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/bin/weechat-curses", "/usr/bin", "weechat")
    #pisitools.dosym("/usr/bin/weechat-curses", "/usr/bin/weechat")
