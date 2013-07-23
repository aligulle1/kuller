#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "Python-%s" % get.srcVERSION()

def setup():
    shelltools.export("OPT", "%(CFLAGS)s -fPIC -D__SOFTFP__" % crosstools.environment)

    crosstools.autoconf()
    crosstools.autoreconf()
    crosstools.autoreconf("-Wcross --verbose --install --force Modules/_ctypes/libffi")
    # pisitools.dosed("Modules/_ctypes/libffi/Makefile.in", r"(^CFLAGS\s*=.*)", "\\1 FFI_DEFAULT_ABI")
    crosstools.configure("--with-fpectl \
                          --enable-shared \
                          --disable-ipv6 \
                          --with-threads \
                          --with-libc='' \
                          --enable-unicode=ucs4 \
                          --with-wctype-functions \
                          --with-pymalloc \
                          --with-cyclic-gc \
                          --with-signal-module \
                          --without-system-ffi")
                          # FIXME: --enable-ipv6
    pisitools.dosed("Makefile", r"\$\{includedir\}", "%(SysRoot)s/usr/include" % crosstools.environment)
    pisitools.dosed("Makefile", r"\$\{libdir\}", "%(SysRoot)s/usr/lib" % crosstools.environment)

def build():
    crosstools.make('HOSTPYTHON=%(ToolchainDir)s/bin/hostpython \
                     HOSTPGEN=%(ToolchainDir)s/bin/hostpgen \
                     BLDSHARED="%(CC)s -shared" \
                     LDSHARED="%(CC)s -shared" \
                     CROSS_COMPILE=%(target)s- \
                     BUILD_SYS="%(build)s" HOST_SYS="%(host)s" \
                     CROSS_COMPILE_TARGET=yes \
                     OPT="%(CFLAGS)s -fPIC -D__SOFTFP__" \
                     libpython2.6.so' % crosstools.environment)

    crosstools.make('HOSTPYTHON=%(ToolchainDir)s/bin/hostpython \
                     HOSTPGEN=%(ToolchainDir)s/bin/hostpgen \
                     BLDSHARED="%(CC)s -shared" \
                     LDSHARED="%(CC)s -shared" \
                     CROSS_COMPILE=%(target)s- \
                     BUILD_SYS="%(build)s" HOST_SYS="%(host)s" \
                     CROSS_COMPILE_TARGET=yes \
                     OPT="%(CFLAGS)s -fPIC -D__SOFTFP__" \
                     ' % crosstools.environment)

def install():
    crosstools.environment["installDIR"] = get.installDIR()

    crosstools.rawInstall('HOSTPYTHON=%(ToolchainDir)s/bin/hostpython \
                           HOSTPGEN=%(ToolchainDir)s/bin/hostpgen \
                           DESTDIR=%(installDIR)s' % crosstools.environment)
    #autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "altinstall")

    #pisitools.dosym("python2.6","/usr/bin/python")
    #pisitools.dosym("python2.6-config","/usr/bin/python-config")
    pisitools.dosym("../lib/python2.6/pdb.py","/usr/bin/pdb")

    pisitools.remove("/usr/bin/idle")
    pisitools.remove("/usr/bin/pydoc")
    pisitools.remove("/usr/bin/smtpd.py")
    pisitools.remove("/usr/bin/2to3")
    pisitools.removeDir("/usr/lib/python2.6/idlelib")

    tkinterFile = "/usr/lib/python2.6/lib-dynload/_tkinter.so"
    if shelltools.isFile("%s/%s" % (get.installDIR(), tkinterFile)):
        pisitools.remove(tkinterFile)
        pisitools.removeDir("/usr/lib/python2.6/lib-tk")

    pisitools.dodoc("LICENSE", "README")
