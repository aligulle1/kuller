#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-xmltoman --disable-subversion")

def build():
    autotools.make()

def install():
    autotools.install()

    # remove init script
    pisitools.remove("/etc/init.d/ifplugd")

    pisitools.dodir("/etc/ifplugd")
    pisitools.dodoc("doc/README", "doc/SUPPORTED_DRIVERS")
    pisitools.dohtml("*.html")
    pisitools.dohtml("*.css")
