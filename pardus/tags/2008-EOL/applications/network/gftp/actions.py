#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.system('./autogen.sh')
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dohtml("README.html")
    pisitools.dodoc("ChangeLog", "COPYING", "README", "THANKS", "TODO", "docs/USERS-GUIDE")
