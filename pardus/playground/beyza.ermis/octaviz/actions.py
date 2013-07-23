#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

WorkDir = "octaviz"

def setup():
    cmaketools.configure("-DVTK_DIR:PATH=/usr/lib/vtk-5.6 \
                          -DVTK_DATA_ROOT:PATH=/usr/lib/vtk-5.6 \
                          -DCMAKE_SKIP_RPATH:BOOL=YES \
                          -DCMAKE_INSTALL_PREFIX:PATH=/usr/bin/octave-config")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "COPYING")





