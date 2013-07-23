#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007,2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

tools = ["sha1pass", "mkdiskimage", "sys2ansi.pl", "keytab-lilo.pl", "syslinux2ansi.pl"]
datadir = "/usr/lib/syslinux"

NoStrip = ["/sbin", "/usr/lib"]

def setup():
    # previously linked to probably some other glibc, better force recompile
    shelltools.unlink("gethostip")
    shelltools.chmod("add_crc", 0755)

def build():
    shelltools.export("CFLAGS", get.CFLAGS())

    autotools.make('DATE="PARDUS" spotless')
    autotools.make('DATE="PARDUS"')

def install():
    autotools.rawInstall('INSTALLROOT=%s MANDIR="/usr/share/man"' % get.installDIR())
    for f in tools:
        pisitools.insinto(datadir, f)

    pisitools.dodoc("README*", "NEWS", "TODO", "doc/*")
