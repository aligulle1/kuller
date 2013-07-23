# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cmaketools.configure("-DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
                        -DCMAKE_VERBOSE_MAKEFILE=ON \
                        -DCMAKE_SKIP_RPATH:BOOL=YES \
                        -DGDCM_BUILD_TESTING=OFF \
                        -DGDCM_BUILD_EXAMPLES:BOOL=ON \
                        -DGDCM_DOCUMENTATION:BOOL=OFF \
                        -DGDCM_PDF_DOCUMENTATION:BOOL=OFF \
                        -DGDCM_WRAP_PYTHON:BOOL=ON \
                        -DGDCM_WRAP_JAVA=OFF \
                        -DGDCM_BUILD_SHARED_LIBS:BOOL=ON \
                        -DGDCM_BUILD_APPLICATIONS:BOOL=ON \
                        -DGDCM_USE_VTK:BOOL=ON \
                        -DGDCM_USE_SYSTEM_CHARLS=ON \
                        -DGDCM_USE_SYSTEM_EXPAT=ON \
                        -DGDCM_USE_SYSTEM_OPENJPEG=ON \
                        -DGDCM_USE_SYSTEM_ZLIB=ON \
                        -DGDCM_USE_SYSTEM_UUID=ON \
                        -DGDCM_USE_SYSTEM_LJPEG=OFF \
                        -DGDCM_USE_SYSTEM_OPENSSL=ON \
                        -DGDCM_USE_JPEGLS=ON \
                        -DGDCM_USE_SYSTEM_JPEGLS=ON \
                        -DGDCM_USE_SYSTEM_POPPLER=ON")


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/lib/gdcm.py", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.domove("/usr/lib/gdcmswig.py", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.domove("/usr/lib/_gdcmswig.so", "/usr/lib/%s/site-packages" % get.curPYTHON())
    pisitools.domove("/usr/lib/vtkgdcm.py", "/usr/lib/%s/site-packages" % get.curPYTHON())

    pisitools.domove("/usr/lib/libvtkgdcmPython.*", "/usr/lib/%s/site-packages" % get.curPYTHON())

    pisitools.domove("/usr/lib/gdcm/*.cmake", "/usr/share/gdcm")
    pisitools.removeDir("/usr/lib/gdcm")

    pisitools.dodoc("README*", "Copyright.txt")

