#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

ver = "1.11"
def setup():
    crosstools.configure()

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Use gnuconfig files
    for config in ["config.guess","config.sub"]:
        pisitools.remove("/usr/share/automake-%s/%s" % (ver, config))
        pisitools.dosym("/usr/share/gnuconfig/%s" % config, "/usr/share/automake-%s/%s" % (ver, config))

    pisitools.dodoc("NEWS", "README", "THANKS", "TODO", "AUTHORS", "ChangeLog*")
