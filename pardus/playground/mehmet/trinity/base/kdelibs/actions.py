#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools

KeepSpecial=["libtool"]

shelltools.export("HOME", get.workDIR())
WorkDir = "%s" % get.srcNAME()
shelltools.export("LC_ALL", "C")
def setup():
    pisitools.dosed("admin/cvs.sh", "automake\*1\.10\*", "automake*1.1[0-5]*")
    pisitools.dosed("admin/acinclude.m4.in", "KDE_CHECK_PYTHON_INTERN\(\"2.5", "KDE_CHECK_PYTHON_INTERN(\"%s" % get.curPYTHON().split("python")[1])
    shelltools.export("LC_ALL", "C")
    kde.make("-f admin/Makefile.common")
    shelltools.system("cp -Rp /usr/share/aclocal/libtool.m4 admin/libtool.m4.in")
    shelltools.system("cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh")
    kde.configure('--with-distribution="Pardus" \
                   --enable-inotify \
                   --enable-cups \
                   --enable-dnssd \
                   --enable-gcc-hidden-visibility \
                   --with-libart \
                   --with-libidn \
                   --with-utempter \
                   --with-alsa \
                   --with-ssl \
                   --with-tiff \
                   --with-gssapi \
                   --with-openexr \
                   --with-jasper \
                   --with-aspell \
                   --with-acl \
                   --disable-libfam \
                   --without-lua \
                   --without-hspell \
                   --with-qt-dir=/usr/qt/3 \
                   --with-qt-includes=/usr/qt/3/include \
                   --with-qt-libraries=/usr/qt/3/lib \
                   --without-arts')

    """
    shelltools.makedirs("build")
    shelltools.cd("build")
    cmaketools.configure("  \
                            -DCMAKE_INSTALL_PREFIX=/usr/kde/3.5 \
                            -DSYSCONFDIR= \
                            -DWITH_LIBIDN=ON -DWITH_SSL=ON -DWITH_LIBART=ON \
                            -DWITH_ALSA=ON -DWITH_ARTS=OFF -DWITH_CUPS=ON \
                            -DWITH_JASPER=ON -DWITH_OPENEXR=ON -DWITH_ASPELL=ON \
                            -DWITH_TIFF=ON -DWITH_LUA=OFF \
                            ", sourceDir="..")
    """

def build():
    shelltools.export("LC_ALL", "C")
    kde.make("-j1")
    #kde.make()
    """
    shelltools.cd("build")
    cmaketools.make()
    """

def install():
    shelltools.export("LC_ALL", "C")
    kde.install()
    """
    shelltools.cd("build")
    cmaketools.install()
    """
