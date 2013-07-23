#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CFLAGS","%s -fPIE" % get.CFLAGS())
    shelltools.export("LDFLAGS", "%s -pie -Wl,-z,relro,-z,now"  % get.LDFLAGS())

    #TODO: Remove KDE prefix
    autotools.configure("--enable-symcryptrun \
                         --disable-rpath \
                         --with-pinentry-pgm=%s/bin/pinentry \
                         --disable-scdaemon \
                         --disable-photo-viewers" % get.kdeDIR())

def build():
    autotools.make("-j1")

    shelltools.cd("doc")
    autotools.make("html")

def install():
    autotools.rawInstall('DESTDIR=%s libexecdir="/usr/libexec"' % get.installDIR())

    pisitools.rename("/usr/share/doc/gnupg", get.srcTAG())

    # Compat symlinks
    pisitools.dosym("/usr/bin/gpg2","/usr/bin/gpg")
    pisitools.dosym("/usr/bin/gpgv2","/usr/bin/gpgv")

    # Lets make doc
    pisitools.dohtml("doc/*")
    pisitools.dohtml("doc/gnupg.html/*")
    pisitools.dodoc("ChangeLog", "NEWS", "README", "THANKS", "TODO")

def check():
    autotools.make("check")
