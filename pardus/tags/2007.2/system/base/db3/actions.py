#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "db-3.2.9"

def setup():
    pisitools.remove("dist/ltversion.sh")
    pisitools.remove("dist/config.guest")
    libtools.gnuconfig_update()
    
    shelltools.makedirs("build-static")
    shelltools.makedirs("build-shared")

    conf = "--host=%s \
            --build=%s \
            --enable-cxx \
            --enable-compat185 \
            --disable-java \
            --prefix=/usr" % (get.HOST(), get.HOST())

    shelltools.cd("build-static")
    shelltools.system("../dist/configure %s --libdir=/usr/lib --enable-static" % conf)

    shelltools.cd("../build-shared")
    shelltools.system("../dist/configure %s --libdir=/usr/lib --enable-dynamic --enable-shared" % conf)


def build():
    shelltools.cd("build-static")
    autotools.make()
    shelltools.cd("../build-shared")
    autotools.make()
            
def install():
    shelltools.cd("build-shared")
    autotools.make("libdb=libdb-3.2.a libcxx=libcxx_3.2.a prefix=%s/usr libdir=%s/usr/lib install" % (get.installDIR(), get.installDIR()))
    
    shelltools.cd("../build-static")

    # slot libraries
    pisitools.dolib_a("libdb.a")
    pisitools.rename("/usr/lib/libdb.a", "libdb-3.2.a")
    pisitools.dolib_a("libdb_cxx.a")
    pisitools.rename("/usr/lib/libdb_cxx.a", "libdb_cxx-3.2.a")

    # create needed symlink
    pisitools.remove("/usr/lib/libdb.so")
    pisitools.remove("/usr/lib/libdb_cxx.so")
    pisitools.dosym("/usr/lib/libdb-3.2.so", "/usr/lib/libdb.so.3")

    # slot all program names to avoid overwriting
    for file in shelltools.ls("%s/usr/bin/db_*" % get.installDIR()):
        sourceFile = file.replace(get.installDIR(), "")
        destinationFile = shelltools.baseName(file.replace("_", "3.2_"))
        destinationDirectory = shelltools.dirName(sourceFile)
        pisitools.domove(sourceFile, destinationDirectory, destinationFile)

    # remove unneeded docs
    pisitools.removeDir("/usr/docs")

    # slot headers
    pisitools.dodir("/usr/include/db3/") 
    pisitools.domove("/usr/include/*.h", "/usr/include/db3/")

    shelltools.cd("../")
    pisitools.dodoc("README", "LICENSE")
