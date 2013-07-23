#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools

WorkDir = "slicer3-r7773"

#shelltools.export("LD_LIBRARY_PATH", "/usr/lib")

def setup():
    cmaketools.configure("-DBUILD_SHARED_LIBS=ON \
                          -DCMAKE_SKIP_RPATH=ON \
                          -DSlicer3_USE_PYTHON:BOOL=ON \
                          -DCMCURL_DIR:PATH=/usr/lib/slicerlibcurl-7.12.1")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s root=%s" % (get.installDIR(), get.installDIR()))

    #add examples
    #pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "Examples")

    #remove Win32 examples
    #pisitools.removeDir("/usr/share/doc/%s/Examples/GUI/Win32" % get.srcTAG())

    #remove Win32 header
    #pisitools.remove("/usr/include/vtk-5.0/vtkWin32Header.h")

    #install python modul
    #shelltools.cd("Wrapping/Python")
    #pythonmodules.install()

