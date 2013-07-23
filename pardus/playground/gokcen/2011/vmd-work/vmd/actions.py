# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="."

def setup():
    shelltools.cd("plugins")
    pisitools.dosed("Make-arch", "CC = gcc", "CC = %s" % get.CC())
    pisitools.dosed("Make-arch", "CCFLAGS =.*\"", "CCFLAGS = %s\"" % get.CFLAGS())
    pisitools.dosed("Make-arch", "CXXFLAGS =.*\"", "CXXFLAGS = %s\"" % get.CXXFLAGS())
    pisitools.dosed("Make-arch", r"CXX = g\+\+", "CXX = %s" % get.CXX())
    pisitools.dosed("Make-arch", "COPTO =.*\"", "COPTO = -fPIC -o\"")
    pisitools.dosed("Make-arch", "LOPTO = .*\"", "LOPTO = %s -fPIC -o\"" % get.LDFLAGS())
    pisitools.dosed("Make-arch", "SHLD = gcc", "SHLD = %s" % get.CC())

    shelltools.cd("../vmd-%s" % get.srcVERSION())
    pisitools.dosed("configure", "gentoo-bindir", "%s/usr/bin" % get.installDIR())
    pisitools.dosed("configure", "gentoo-libdir", "%s/usr/lib" % get.installDIR())
    pisitools.dosed("configure", "gentoo-opengl-include", "/usr/include/GL")
    pisitools.dosed("configure", "gentoo-opengl-libs", "/usr/lib")

    pisitools.dosed("configure", "gentoo-gcc", get.CC())
    pisitools.dosed("configure", r"gentoo-g\+\+", get.CXX())
    pisitools.dosed("configure", "gentoo-cflags", get.CFLAGS())
    pisitools.dosed("configure", "gentoo-cxxflags", get.CXXFLAGS())
    pisitools.dosed("configure", "gentoo-ldflags", get.LDFLAGS())

    pisitools.dosed("configure", "gentoo-plugindir", "%s/%s/plugins" % (get.workDIR(), WorkDir))
    pisitools.dosed("configure", "gentoo-fltk-include", "/usr/include")
    pisitools.dosed("configure", "gentoo-fltk-libs", "/usr/lib")
    pisitools.dosed("configure", "gentoo-netcdf-include", "/usr/include/netcdf")
    pisitools.dosed("configure", "gentoo-netcdf-libs", "/usr/lib")

    pisitools.dosed("configure", "gentoo-python-include", "/usr/include/%s" % get.curPYTHON())
    pisitools.dosed("configure", "gentoo-python-lib", "/usr/lib")
    pisitools.dosed("configure", "gentoo-python-link", get.curPYTHON())
    pisitools.dosed("configure", "gentoo-numpy-include", "/usr/lib/%s/site-packages/numpy/core/include" % get.curPYTHON())

    pisitools.dosed("bin/vmd.sh", "LINUXPPC", "LINUX")
    pisitools.dosed("bin/vmd.sh", "LINUXALPHA", "LINUX")
    pisitools.dosed("bin/vmd.sh", "LINUXAMD64", "LINUX")

    # Fix temp directory
    pisitools.dosed("scripts/vmd/vmdinit.tcl", "/usr/tmp", "/tmp")

    options = 'LINUX OPENGL FLTK TK TCL PTHREADS PYTHON IMD NETCDF NUMPY NOSILENT '
    f = open("configure.options", "w")
    f.write(options)
    f.close()

    autotools.rawConfigure()

def build():
    shelltools.cd("plugins")
    autotools.make('-j1 LINUX TCLINC="-I/usr/include" \
                              TCLLIB="-L/usr/lib" \
                              NETCDFLIB="-L/usr/lib" \
                              NETCDFINC="-I/usr/include/netcdf" \
                              NETCDFLDFLAGS="-lnetcdf"')

    shelltools.cd("../vmd-%s/src" % get.srcVERSION())
    autotools.make()

def install():
    shelltools.cd("plugins")
    shelltools.export('PLUGINDIR', "%s/usr/lib/vmd/plugins" % get.installDIR())
    autotools.make("-j1 distrib")

    shelltools.cd("../vmd-%s/src" % get.srcVERSION())
    autotools.install()

    shelltools.cd("..")
    pisitools.dodoc("Announcement", "LICENSE", "README", "doc/ug.pdf")

    for f in ("Announcement", "LICENSE", "README"):
        pisitools.remove("/usr/lib/vmd/%s" % f)
    pisitools.removeDir("/usr/lib/vmd/doc")

    pisitools.dosed("%s/usr/bin/vmd" % get.installDIR(), get.installDIR())
