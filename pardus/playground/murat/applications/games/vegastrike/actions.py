#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-release=2 \
                         --enable-client \
                         --disable-static \
                         --enable-gtk \
                         --enable-sdl \
                         --enable-sdl-windowing \
                         --enable-sound \
                         --enable-vorbis \
                         --enable-ffmpeg \
                         --enable-nvidia-cg \
                         --with-python-version=2.5 \
                         --enable-flags='-Wno-deprecated \
                         -DBOOST_PYTHON_NO_PY_SIGNATURES %s' \
                         --with-boost=system \
                         --with-data-dir=/usr/share/vegastrike"
                         % get.CXXFLAGS())

def build():
    autotools.make()

    shelltools.cd("setup/src")
    autotools.make()

def install():
    autotools.install()

    pisitools.dobin("setup/src/vssetup.bin")
    pisitools.rename("/usr/bin/vegastrike", "vegastrike.bin")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "DOCUMENTATION", "NEWS", "README", "*.txt")
