#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "dopuskh3-openFrameworks-fbe8e6c"

# closed? what closed?
# https://github.com/openframeworks/openFrameworks/pull/242

# dopuskh3's blog
# http://digitalork.blogspot.com/

# A cmake port of openFrameworks for build with CCV-COT version
# and fork of dopuskh3 (Francois Visconte) openFrameworks cmake port
# https://bitbucket.org/b2ag/openframeworks-cmake

# CCV-COT
# http://code.google.com/p/ccv-tt/

def setup():
    shelltools.cd("libs/openFrameworks")

    cmaketools.configure()

def build():
    shelltools.cd("libs/openFrameworks")

    cmaketools.make()

def install():
    shelltools.cd("libs/openFrameworks")

    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
