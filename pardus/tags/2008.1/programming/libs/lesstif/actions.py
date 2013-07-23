#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    libtools.libtoolize("--force --copy")

    autotools.configure("--enable-production \
                         --enable-verbose=no \
                         --with-x")

    pisitools.dosed("libtool", "^(hardcode_into_libs)=.*", "hardcode_into_libs=no")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

    for i in ["mwm", "mxmkmf", "uil", "xmbind"]:
        pisitools.domove("/usr/bin/%s" % i , "/usr/lib/lesstif-2.1")

    for i in ["libDtPrint.so", "libDtPrint.so.1.0.0", "libMrm.so", "libMrm.so.2.0.1",
              "libUil.so", "libUil.so.2.0.1", "libXm.so", "libXm.so.2.0.1",
              "libDtPrint.la", "libDtPrint.so.1", "libMrm.la", "libMrm.so.2",
              "libUil.la", "libUil.so.2", "libXm.la", "libXm.so.2"]:
        pisitools.domove("/usr/lib/%s" % i, "/usr/lib/lesstif-2.1")

    for i in ["Dt", "Mrm","uil", "Xm"]:
        pisitools.domove("/usr/include/%s" % i, "/usr/include/lesstif-2.1")

    """
    for i in [1, 3, 5]:
        pisitools.dodir("/usr/share/man/man%s" % i)
        pisitools.domove("", "/usr/share/man/man%s" % i)

    einfo "Fixing man pages"
    mans="1 3 5"
    for man in $mans; do
        dodir /usr/share/man/man${man}
        for file in `ls ${D}/usr/share/man/man${man}`
        do
            file=${file/.${man}/}
            mv ${D}/usr/share/man/man$man/${file}.${man} ${D}/usr/share/man/man${man}/${file}-lesstif-1.2.${man}
        done
    done
    """

    pisitools.domove("/usr/LessTif/*", "/usr/share/doc/%s/" % get.srcTAG())

    pisitools.dodir("/usr/lib/motif")
    pisitools.dodir("/etc/X11/mwm")
    #pisitools.dosym("../../usr/lib/X11/mwm", "/etc/X11/mwm")

    pisitools.removeDir("/usr/lib/LessTif")
    pisitools.remove("/usr/lib/lesstif-2.1/mxmkmf")
    pisitools.removeDir("/usr/share/aclocal")
    pisitools.removeDir("/usr/lib/LessTif")
