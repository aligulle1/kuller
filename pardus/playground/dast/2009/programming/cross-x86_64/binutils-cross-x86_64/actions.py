#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "binutils-%s" % get.srcVERSION()
NoStrip = "/"

host = "i686-cross-linux-gnu"
target = "x86_64-unknown-linux-gnu"
prefix = "/opt/cross-x86_64"
build_dir = "../build"

def set_env():
    shelltools.export("CFLAGS", "")
    shelltools.export("CXXFLAGS", "")
    shelltools.export("AS", "as")
    shelltools.export("AR", "ar")

def setup():
    set_env()
    shelltools.makedirs(build_dir)
    shelltools.cd(build_dir)
    shelltools.system("../%s/configure --prefix=%s " \
        "--host=%s --target=%s --with-lib-path=%s/lib " \
        "--disable-nls --enable-shared --enable-64-bit-bfd" \
        % (WorkDir, prefix, host, target, prefix))

def build():
    set_env()
    shelltools.cd(build_dir)
    autotools.make()

def install():
    pisitools.insinto("/opt/cross-x86_64/include", "include/libiberty.h", "libiberty.h")
    shelltools.cd(build_dir)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/opt/cross-x86_64/info/*")
