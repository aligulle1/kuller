#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-release \
                         --with-parallel-make=auto \
                         --with-root-dir=%s" % get.installDIR())

def build():
    autotools.make("QTDIR=%s" % get.qtDIR())

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
