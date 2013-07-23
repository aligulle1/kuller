#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="util-linux-2.13-pre7"

def setup():
    pisitools.dosed("mount/Makefile.in", "chmod 4755", "chmod 4711")
    
    autotools.rawConfigure("--prefix=/ \
                            --enable-nls \
                            --without-pam \
                            --enable-agetty \
                            --enable-cramfs \
                            --disable-init \
                            --disable-kill \
                            --disable-last \
                            --disable-mesg \
                            --enable-partx \
                            --enable-raw \
                            --enable-rdev \
                            --enable-rename \
                            --disable-reset \
                            --disable-login-utils \
                            --enable-schedutils \
                            --disable-wall \
                            --enable-write")

def build():
    autotools.make()
    
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("HISTORY", "MAINTAINER", "README", "VERSION", "example.files/*")

    # Conflicts with schedutils package
    pisitools.remove("/usr/bin/taskset")
    pisitools.remove("/usr/bin/chrt")
    pisitools.remove("/usr/bin/ionice")
    pisitools.remove("/usr/share/man/man1/chrt.1")
    pisitools.remove("/usr/share/man/man1/taskset.1")
