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

version = get.srcVERSION().replace(".","-")
WorkDir = "Singular-%s" % version


def setup():
    shelltools.export("LDFLAGS", "")
    pisitools.dosed("Singular/configure","--no-exceptions","")
    pisitools.dosed("kernel/feResource.cc","PFSUBST", get.srcTAG())

    autotools.rawConfigure("--disable-doc \
                           --without-MP \
                           --with-factory \
                           --with-libfac \
                           --with-gmp \
                           --prefix=%s/build" % get.curDIR())

def build():
    autotools.make("-j1")

def install():

    autotools.rawInstall("DESTDIR=%s" % get.installDIR()) 



    for data in ["*.lib","help.cnf"]:
        shelltools.chmod("build/LIB/%s" % data, 0644)
        pisitools.insinto("/usr/share/singular/lib","build/LIB/%s" % data)

    for data in ["build/LIB/gftables/*"]:
        shelltools.chmod(data, 0644)
        pisitools.insinto("/usr/share/singular/lib/gftables", data)

    for data in ["*.el",".emacs*"]:
        pisitools.insinto("/usr/share/singular/emacs", "emacs/%s" % data)

    for bin in ["Singular-*","gen_test","change_cost","solve_IP","toric_ideal","LLL"]:
        pisitools.dobin("build/*-Linux/%s" % bin)

    pisitools.dolib("build/*-Linux/*.so")
    pisitools.dosym("/usr/bin/Singular-%s" % version , "/usr/bin/Singular")


    pisitools.removeDir("/usr/share/singular/lib/gftables/CVS")

    pisitools.dodoc("ChangeLog", "COPYING","doc/*.doc")
