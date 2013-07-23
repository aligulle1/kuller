#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2..
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

WorkDir="VTK"

shelltools.export("LD_LIBRARY_PATH", "/usr/lib")

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON \
                          -DVTK_DIR=/usr/lib/vtk-5.6 \
                          -DVTK_USE_SYSTEM_EXPAT=ON \
                          -DVTK_USE_SYSTEM_FREETYPE=ON \
                          -DVTK_USE_SYSTEM_JPEG=ON \
                          -DVTK_USE_SYSTEM_LIBXML2=ON \
                          -DVTK_USE_SYSTEM_PNG=ON \
                          -DVTK_USE_SYSTEM_TIFF=ON \
                          -DVTK_USE_SYSTEM_ZLIB=ON \
                          -DVTK_USE_HYBRID=ON \
                          -DVTK_USE_GL2PS=ON \
                          -DVTK_USE_RENDERING=ON \
                          -DVTK_USE_BOOST=ON \
                          -DVTK_USE_QT=ON \
                          -DVTK_WRAP_TCL=ON \
                          -DVTK_USE_OGGTHEORA_ENCODER=ON \
                          -DVTK_USE_FFMPEG_ENCODER=ON \
                          -DVTK_USE_GNU_R=ON \
                          -DR_LIBRARY_BLAS=/usr/lib \
                          -DR_LIBRARY_LAPACK=/usr/lib \
                          -DBUILD_TESTING=OFF \
                          -DVTK_WRAP_PYTHON=ON \
                          -DPYTHON_INCLUDE_PATH=/usr/include/python2.6 \
                          -DVTK_USE_GUISUPPORT=ON \
                          -DVTK_USE_QVTK=ON \
                          -DQT_WRAP_CPP=ON \
                          -DQT_WRAP_UI=ON \
                          -DVTK_INSTALL_QT_DIR=/qt/4/plugins \
                          -DVTK_DATA_ROOT=/usr/share/%s/data" % get.srcTAG())

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s root=%s" % (get.installDIR(), get.installDIR()))
 
    #add examples
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "Examples")

    #remove Win32 examples
    pisitools.removeDir("/usr/share/doc/%s/Examples/GUI/Win32" % get.srcTAG())

    #remove Win32 header
    pisitools.remove("/usr/include/vtk-5.0/vtkWin32Header.h")
    
    #install python modul
    shelltools.cd("Wrapping/Python")
    pythonmodules.install() 
