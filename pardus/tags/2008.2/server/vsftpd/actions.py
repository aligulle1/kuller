#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.echo("#define VSF_BUILD_TCPWRAPPERS", "builddefs.h")
    shelltools.echo("#define VSF_BUILD_SSL", "builddefs.h")
    shelltools.echo("#undef VSF_BUILD_PAM", "builddefs.h")

def build():
    autotools.make('CC="%s" CFLAGS="%s -fpie" LINK="-pie"' % (get.CC(),get.CFLAGS()))

def install():
    pisitools.dosbin("vsftpd")

    pisitools.dodir("/home/ftp")
    pisitools.dodir("/home/ftp/incoming")
    pisitools.dodir("/usr/share/vsftpd/empty")

    pisitools.newdoc("vsftpd.conf", "vsftpd.conf.example")
    pisitools.doman("vsftpd.conf.5", "vsftpd.8")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "SECURITY")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "EXAMPLE")
    pisitools.dodoc("AUDIT", "BENCHMARKS", "BUGS", "Changelog", "FAQ",\
                    "LICENSE", "README*", "REFS", "REWARD", "SIZE", \
                    "SPEED", "TODO", "TUNING")
