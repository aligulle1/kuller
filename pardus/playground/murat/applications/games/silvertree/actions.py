#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import scons
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-boost-regex=boost_regex")

    pisitools.dosed("Makefile", "doc/\${PACKAGE_TARNAME}", "doc/%s" % get.srcTAG())

def build():
    autotools.make()

    # Build silvertree map editor
    scons.make("QTDIR=/usr/qt/4 \
                Build=release \
                editor")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("build/release/editor/silvertreeedit")
