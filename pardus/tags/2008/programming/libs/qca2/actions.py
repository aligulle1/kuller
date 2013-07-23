#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = 'qca-%s' % (get.srcVERSION())
Suffix = '%s-%s' % (get.srcVERSION(), get.srcRELEASE())

def setup():
    autotools.rawConfigure("--prefix=/usr --qtdir=/usr/qt/4")

def build():
    autotools.make()
    autotools.make("apidox")

def install():
    autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # Put apidocs in its own directory
    pisitools.dodir("/usr/share/doc/qca2-apidocs-%s/html" % Suffix)
    pisitools.insinto("/usr/share/doc/qca2-apidocs-%s/html" % Suffix, "apidocs/html/*")

    pisitools.dodoc("README", "TODO", "COPYING")
