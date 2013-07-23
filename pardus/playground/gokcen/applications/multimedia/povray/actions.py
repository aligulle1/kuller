#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
import os

def setup():
    autotools.aclocal()
    autotools.autoconf()

    # no svga dep. yet
    #FIXME svgalibs dep.
    autotools.configure("--without-svga --with-x COMPILED_BY=\"Pardus\"")

def build():
    #FIXME copy povray.ini and povray.conf to user's home also
    pisitools.dosed("Makefile", "^povconfuser = .*", "povconfuser = %s/etc/skel/.povray/3.6/" % get.installDIR())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
