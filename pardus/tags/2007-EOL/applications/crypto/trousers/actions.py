#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure("--disable-static --enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc", "/dist/tcsd.conf")
    pisitools.chmod("%s/etc/tcsd.conf" % get.installDIR(), 0600)
    pisitools.dobin("tools/ps_convert", "/usr/share/doc/%s/tools" % get.srcTAG())
    pisitools.dobin("tools/ps_inspect", "/usr/share/doc/%s/tools" % get.srcTAG())
    pisitools.dodoc("README","AUTHORS", "ChangeLog","NICETOHAVES","TODO")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "doc/*")

    pisitools.dodir("/var/lib/tpm")
