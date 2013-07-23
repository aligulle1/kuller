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

def prepare_environment():
    crosstools.environment["CXXFLAGS"] = ""
    crosstools.environment["instDIR"] = get.installDIR()
    crosstools.environment["workDIR"] = get.workDIR()
    crosstools.environment["srcVER"] = get.srcVERSION()
    crosstools.environment["CFLAGS"] = "-Du32=__u32 -O2 \
                                        -I%(workDIR)s/iproute2-%(srcVER)s/include/linux \
                                        -I%(workDIR)s/iproute2-%(srcVER)s/include/ \
                                        -I%(RootDir)s/usr/include \
                                        -L%(RootDir)s/usr/lib -L%(RootDir)s/lib" % crosstools.environment
    crosstools.environment["LDFLAGS"] = "%(LDFLAGS)s -L%(RootDir)s/usr/lib -L%(RootDir)s/lib"  % crosstools.environment

def setup():
    pisitools.dosed("configure", "gcc", "%(CC)s" % crosstools.environment)
    crosstools.configure()

def build():
    shelltools.export("LC_ALL", "C")
    prepare_environment()
    crosstools.prepare()

    crosstools.make('CC="%(CC)s" \
                     KERNEL_INCLUDE="%(SysRoot)s/usr/include" \
                     RPM_OPT_FLAGS="%(CFLAGS)s" \
                     SUBDIRS="lib tc ip" \
                     CFLAGS="%(CFLAGS)s" \
                     LDFLAGS="%(LDFLAGS)s"' % crosstools.environment)

def install():
    prepare_environment()

    # FIXME: something's missing.
    crosstools.rawInstall('DESTDIR="%(instDIR)s" \
                           SBINDIR="/sbin" \
                           DOCDIR="/%(docDIR)s" \
                           MANDIR="/usr/share/man" \
                           ROOTDIR="%(SysRoot)s" \
                           SUBDIRS="lib tc ip"' % crosstools.environment)

    pisitools.removeDir("/var")
    #pisitools.dodir("/usr/sbin")
    #pisitools.dodir("/var/lib/arpd")
