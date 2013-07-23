#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file `http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import get

BLENDERAPI = "2.60"

def setup():
    # Drop bundled libraries
    for d in ["glew", "libopenjpeg", "Eigen2"]:
        shelltools.unlinkDir("extern/%s" % d)

    shelltools.unlinkDir("scons")

    shelltools.makedirs("build")
    shelltools.cd("build")

    #it seems new blender requires ffmpeg 0.7 or newer
    cmaketools.configure("-DCMAKE_SKIP_RPATH=ON \
                          -DBUILD_SHARED_LIBS=OFF \
                          -DWITH_FFTW3=ON \
                          -DWITH_JACK:BOOL=ON \
                          -DWITH_CODEC_SNDFILE:BOOL=ON \
                          -DWITH_IMAGE_OPENJPEG:BOOL=ON \
                          -DWITH_PYTHON:BOOL=ON \
                          -DWITH_PYTHON_INSTALL:BOOL=OFF \
                          -DWITH_CODEC_FFMPEG:BOOL=OFF \
                          -DWITH_GAMEENGINE:BOOL=ON \
                          -DWITH_CXX_GUARDEDALLOC:BOOL=OFF \
                          -DWITH_BUILTIN_GLEW=OFF \
                          -DWITH_INSTALL_PORTABLE=OFF \
                          -DWITH_PYTHON_SAFETY=ON \
                          -DWITH_PLAYER=ON", sourceDir = "..")

def build():
    shelltools.cd("build")
    cmaketools.make()
    shelltools.cd("..")

    shelltools.makedirs("release/plugins/include")
    shelltools.copy("source/blender/blenpluginapi/*.h", "release/plugins/include")

    shelltools.chmod("release/plugins/bmake", 0755)
    cmaketools.make("-C release/plugins")

def install():
    shelltools.cd("build")

    # Blender uses versioned paths (like /usr/share/blender/2.60) in the code (i.e source/blender/blenlib/intern/path_util.c)
    # so do not try to patch all those instances to move blender into a unversioned path
    cmaketools.install()

    shelltools.cd("..")

    blenderdir = "/usr/share/blender/%s" % BLENDERAPI

    # Install plugins
    for d in ("%s/scripts" % blenderdir, "%s/plugins/sequence" % blenderdir, "%s/plugins/texture" % blenderdir):
        pisitools.dodir(d)

    pisitools.insinto("%s/plugins/texture" % blenderdir, "release/plugins/texture/*.so")
    pisitools.insinto("%s/plugins/sequence" % blenderdir, "release/plugins/sequence/*.so")

    pisitools.insinto("/usr/share", "release/bin/.blender/locale")

    # chmod 644 for scripts
    #shelltools.chmod("%s/usr/share/blender/scripts/*.py" % get.installDIR(), 0644)

    # Headers
    pisitools.insinto("/usr/include/blender", "release/plugins/include/*.h")

    pisitools.dodoc("COPYING")
