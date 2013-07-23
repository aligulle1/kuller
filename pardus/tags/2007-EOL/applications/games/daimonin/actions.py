#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "daimonin_client-%s/make/linux" % get.srcVERSION()

def setup():
    shelltools.chmod("configure", 0755)
    autotools.configure("-disable-simplelayout")

def build():
    autotools.make("all")

def install():
    autotools.install()
    pisitools.remove("/usr/bin/updater")

    pisitools.dodoc("License", "README")
