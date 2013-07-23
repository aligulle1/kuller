#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

version='0.54'
revision='654'

def setup():

    # Setup version.sh
    shelltools.unlink("version.sh")
    shelltools.echo('version.sh','echo "#define X264_VERSION  \\"svn-%s\\"" >> config.h' % revision)
    shelltools.echo('version.sh','echo "#define X264_POINTVER \\"%s.%s\\"" >> config.h' % (version,revision))
    shelltools.chmod("version.sh")

    autotools.rawConfigure("--prefix=/usr \
                            --enable-pthread \
                            --enable-shared \
                            --enable-pic \
                            --enable-mp4-output")

def build():
    autotools.make()

def install():
    autotools.install()

    # No static libs
    pisitools.remove("/usr/lib/libx264.a")
