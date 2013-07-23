#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "%s -Wl,-z,now"  % get.LDFLAGS())
    autotools.configure("--enable-agent \
                         --enable-noexecstack \
                         --enable-symcryptrun \
                         --enable-ldap \
                         --enable-gpgsm \
                         --enable-hkp \
                         --enable-finger \
                         --with-libcurl \
                         --enable-nls \
                         --enable-bzip2 \
                         --with-pinentry-pgm=/usr/kde/3.5/bin/pinentry \
                         --disable-scdaemon \
                         --disable-photo-viewers \
                         --disable-capabilities \
                         --with-readline \
                         --enable-static-rnd=linux \
                         --libexecdir=/usr/libexec \
                         --enable-sha51")

def build():
    autotools.make()
    shelltools.cd("doc")
    autotools.make("html")

def install():
    autotools.rawInstall("DESTDIR=%s libexecdir=\"/usr/libexec\"" % get.installDIR())

    # keep the documentation in /usr/share/doc/...
    pisitools.remove("/usr/share/gnupg/FAQ")
    pisitools.remove("/usr/share/gnupg/faq.html")

    # Lets make doc
    pisitools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO", "VERSION")
    pisitools.insinto("/usr/share/doc/%s/html" % get.srcTAG(), "doc/faq.html")
    pisitools.insinto("/usr/share/doc/%s/html" % get.srcTAG(), "doc/gnupg-card-architecture.png")
    pisitools.dohtml("doc/gnupg.html/*")

    # Compat symlinks
    pisitools.dosym("/usr/bin/gpg2","/usr/bin/gpg")
    pisitools.dosym("/usr/bin/gpgv2","/usr/bin/gpgv")
