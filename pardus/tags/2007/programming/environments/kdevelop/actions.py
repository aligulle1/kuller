#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    # Update the admin dir used in KDE template projects.
    for i in shelltools.ls("admin/*"):
        shelltools.copy(i, "parts/appwizard/common/admin/")

    # copy system's ltmain.sh over old one
    shelltools.copy("/usr/share/libtool/ltmain.sh", "parts/appwizard/common/admin/")
    shelltools.copy("/usr/share/libtool/ltmain.sh", "parts/appwizard/common/incadmin/")

    kde.configure("--with-kdelibsdoxy-dir=%s/share/doc/HTML/en/kdelibs-apidocs \
                   --enable-java \
                   --enable-python \
                   --enable-ruby \
                   --enable-ada \
                   --enable-fortran \
                   --enable-haskell \
                   --enable-pascal \
                   --enable-perl \
                   --enable-php \
                   --enable-sql \
                   --enable-antproject \
                   --enable-subversion" % get.kdeDIR())

def build():
    kde.make()

def install():
    kde.install()
