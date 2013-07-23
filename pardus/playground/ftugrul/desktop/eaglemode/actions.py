#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("eaglemode.sh", "\`pwd\`", "/usr/share/eaglemode")

def build():
    shelltools.system("perl make.pl build")

def install():
    shelltools.system("perl make.pl install dir=%s/usr/share/eaglemode" % get.installDIR())
    pisitools.domove("/usr/share/eaglemode/lib/*", "/usr/lib/")
    pisitools.domove("/usr/share/eaglemode/include/*", "/usr/include/")
    pisitools.domove("/usr/share/eaglemode/eaglemode.sh", "/usr/bin/", "eaglemode")
    pisitools.dosym("/usr/share/eaglemode/res/icons/eaglemode32.png", "/usr/share/pixmaps/eaglemode.png")

    pisitools.domove("/usr/share/eaglemode/doc/html/*", "/usr/share/doc/eaglemode/")
    pisitools.domove("/usr/share/eaglemode/README", "/usr/share/doc/eaglemode/")
