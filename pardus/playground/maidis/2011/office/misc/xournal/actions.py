#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    shelltools.export("CC", get.CC())
    shelltools.system("./autogen.sh")

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("desktop-install DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/mimelnk")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
