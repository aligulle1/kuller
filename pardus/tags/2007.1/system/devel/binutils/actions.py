#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "binutils-2.16.1/"

libpath = "/usr/lib/binutils/%s/%s" % (get.HOST(), get.srcVERSION())
incpath = libpath + "/include"
binpath = "/usr/%s/binutils-bin/%s" % (get.HOST(), get.srcVERSION())
datapath = "/usr/share/binutils-data/%s/%s" % (get.HOST(), get.srcVERSION())

def setup():
    for f in shelltools.ls("*/po/Make-in"):
        pisitools.dosed(f, "(?m)^(datadir = )$(prefix)/@DATADIRNAME@", r"@datadir@")
        pisitools.dosed(f, "(?m)^(gnulocaledir = )$(prefix)/share", r"$(datadir)")

    libtools.gnuconfig_update()

    conf = "--without-included-gettext \
            --disable-nls \
            --host=%s \
            --target=%s\
            --datadir=%s \
            --infodir=%s/info \
            --mandir=%s/man \
            --bindir=%s \
            --libdir=%s \
            --libexecdir=%s \
            --includedir=%s \
            --enable-shared \
            --disable-werror" % (get.HOST(), get.HOST(), datapath, datapath,\
                datapath, binpath, libpath, libpath, incpath)

    shelltools.makedirs("%s/build-default-i686-pc-linux-gnu-nptl" % get.workDIR())
    shelltools.cd("%s/build-default-i686-pc-linux-gnu-nptl" % get.workDIR())
    shelltools.system("%s/%s/configure %s" % (get.workDIR(), WorkDir, conf))

def build():
    shelltools.cd("%s/build-default-i686-pc-linux-gnu-nptl" % get.workDIR())

    autotools.make("-j1 configure-bfd")
    autotools.make("-j1 headers -C bfd")
    autotools.make("all")
    autotools.make("info")
    
def install():
    shelltools.cd("%s/build-default-i686-pc-linux-gnu-nptl" % get.workDIR())

    autotools.rawInstall("DESTDIR=%s tooldir=%s" % (get.installDIR(), libpath))

    pisitools.removeDir("%s/bin" % libpath)
    pisitools.insinto(incpath, "include/libiberty.h")
    pisitools.domove("%s/lib/ldscripts/" % libpath, "%s/ldscripts" % libpath)
    pisitools.removeDir(libpath + "/lib")

    pisitools.dodir("/usr/%s/lib" % get.HOST())

    pisitools.dodoc("README")

    # create /usr/bin/* --> /usr/i686-pc-linux-gnu/binutils-bin/2.16.1/nm
    for bin in shelltools.ls("%s/usr/%s/binutils-bin/%s/" % (get.installDIR(), get.HOST(), get.srcVERSION())):
        pisitools.dosym("/usr/%s/binutils-bin/%s/%s" % (get.HOST(), get.srcVERSION(), bin), \
            "/usr/bin/%s-%s" % (get.HOST(), bin))

        pisitools.dosym("/usr/%s/binutils-bin/%s/%s" % (get.HOST(), get.srcVERSION(), bin), \
            "/usr/bin/%s" % (bin))

    # create usr/i686-pc-linux-gnu/lib/* --> /usr/lib/binutils/i686-pc-linux-gnu/2.16.1/* links
    for lib in shelltools.ls("%s/usr/lib/binutils/%s/%s/" % (get.installDIR(), get.HOST(), get.srcVERSION())):
        pisitools.dosym("/usr/lib/binutils/%s/%s/%s" % (get.HOST(), get.srcVERSION(), lib), \
            "/usr/%s/lib/%s" % (get.HOST(), lib))

    pisitools.remove("/usr/%s/lib/include" % get.HOST())
    
    shelltools.cd("%s/%s" % (get.workDIR(), WorkDir))
    
    # Handle documentation
    pisitools.newdoc("bfd/README", "bfd/README") 
    pisitools.newdoc("bfd/PORTING", "bfd/PORTING") 
    pisitools.newdoc("bfd/TODO", "bfd/TODO") 
    pisitools.newdoc("binutils/ChangeLog", "binutils/ChangeLog") 
    pisitools.newdoc("binutils/NEWS", "binutils/NEWS") 
    pisitools.newdoc("binutils/README", "binutils/README") 
    pisitools.newdoc("gas/CONTRIBUTORS", "gas/CONTRIBUTORS") 
    pisitools.newdoc("gas/NEWS", "gas/NEWS") 
    pisitools.newdoc("gas/README", "gas/README") 
    pisitools.newdoc("gas/README-vms", "gas/README-vms")
    pisitools.newdoc("gprof/ChangeLog", "gprof/ChangeLog") 
    pisitools.newdoc("gprof/ChangeLog.linux", "gprof/ChangeLog.linux") 
    pisitools.newdoc("gprof/TEST", "gprof/TEST")
    pisitools.newdoc("gprof/TODO", "gprof/TODO")
    pisitools.newdoc("gprof/bbconv.pl", "gprof/bbconv.pl")
    pisitools.newdoc("ld/README", "ld/README")
    pisitools.newdoc("ld/NEWS", "ld/NEWS")  
    pisitools.newdoc("ld/TODO", "ld/TODO")
    pisitools.newdoc("libiberty/ChangeLog.linux", "libiberty/ChangeLog.linux")
    pisitools.newdoc("libiberty/ChangeLog", "libiberty/ChangeLog")
    pisitools.newdoc("libiberty/README", "libiberty/README")

