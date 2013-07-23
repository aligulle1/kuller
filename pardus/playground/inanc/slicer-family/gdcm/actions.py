#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.makedirs("../build/")
    shelltools.cd("../build/")
    cmaketools.configure("-DCMAKE_SKIP_RPATH:BOOL=YES \
                          -DGDCM_BUILD_APPLICATIONS:BOOL=ON \
                          -DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
                          -DSWIG_DIR:PATH=/usr \
                          -DSWIG_EXECUTABLE:FILEPATH=/usr/bin/swig \
                          -DGDCM_DOCUMENTATION:BOOL=ON \
                          -DGDCM_BUILD_EXAMPLES:BOOL=ON \
                          -DGDCM_USE_SYSTEM_EXPAT:BOOL=ON \
                          -DGDCM_USE_SYSTEM_ZLIB:BOOL=ON \
                          -DGDCM_WRAP_JAVA:BOOL=OFF \
                          -DGDCM_WRAP_PYTHON:BOOL=ON \
                          -DGDCM_USE_VTK:BOOL=ON \
                          -DVTK_DIR:PATH=/usr/lib/vtk-5.2 \
                          -DGDCM_USE_SYSTEM_OPENJPEG:BOOL=ON \
                          -DOPENJPEG_INCLUDE_DIR:PATH=/usr/include/openjpeg/ \
                          -DGDCM_USE_WXWIDGETS:BOOL=ON \
                          -DGDCM_PDF_DOCUMENTATION:BOOL=OFF", sourceDir="../%s" % get.srcDIR())

def build():
    shelltools.cd("../build/")
    cmaketools.make("-j1")

def install():
    shelltools.cd("../build/")
    cmaketools.rawInstall("DESTDIR=%s root=%s" % (get.installDIR(), get.installDIR()))

    pisitools.dohtml("%s/build/Utilities/doxygen/html/*" % get.workDIR())
    pisitools.doman("%s/build/Utilities/doxygen/man/man1/*" % get.workDIR())
    pisitools.remove("/usr/share/man/man1/_*")

    pisitools.dodir("/usr/lib/python2.5/site-packages/gdcm/")
    pisitools.domove("/usr/lib/*.py", "/usr/lib/python2.5/site-packages/gdcm/")

    pisitools.dodoc("AUTHORS", "Copyright.txt", "README.txt")
