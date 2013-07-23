#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "ladspa_sdk/src"

_build="i686-pc-linux-gnu"
_host="arm-cortex_a8-linux-gnueabi"
_target=_host

# ugly hard-coded stuff, unfortunately..
_RootDir="/pardus-arm"
_ToolchainDir = "/home/memre/x-tools"

# Pardus-ARM preparation
def prepare():
    shelltools.export("LC_ALL", "C")
    shelltools.export("CXXFLAGS", "-I%s/usr/include -L%s/usr/lib -L%s/lib" % (_RootDir, _RootDir, _RootDir))
    shelltools.export("CFLAGS",   "-I%s/usr/include -L%s/usr/lib -L%s/lib" % (_RootDir, _RootDir, _RootDir))
    shelltools.export("LDFLAGS",  "-L%s/usr/lib -L%s/lib" % (_RootDir, _RootDir))

    shelltools.export("CC",     "%s-gcc" % _target)
    shelltools.export("CXX",    "%s-g++" % _target)
    shelltools.export("AR",     "%s-ar"  % _target)
    shelltools.export("AS",     "%s-as"  % _target)
    shelltools.export("LD",     "%s-ld"  % _target)
    shelltools.export("RANLIB", "%s-ranlib"  % _target)
    shelltools.export("OBJDUMP","%s-objdump" % _target)
    shelltools.export("STRIP",  "%s-strip"   % _target)
    shelltools.export("LIBTOOL","%s-libtool" % _target)

def setup():
    # Pardus-ARM preparation
    prepare()

    pisitools.dosed("makefile", "-Werror", get.CFLAGS())

def build():
    # Pardus-ARM preparation
    prepare()

    autotools.make('CC="%s" \
                    CXX="%s" \
                    LD="%s" \
                    targets' % (get.CC(), get.CXX(), get.LD()))

def install():
    autotools.install('INSTALL_PLUGINS_DIR="/usr/lib/ladspa" \
                       MKDIR_P="mkdir -p" \
                       DESTDIR="%s"' % get.installDIR())

    shelltools.cd("..")
    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("doc/COPYING","doc/ladspa.h.txt")
