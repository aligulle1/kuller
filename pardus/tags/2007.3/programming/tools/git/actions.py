#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # Use our flags
    pisitools.dosed("Makefile", "^CFLAGS =.*", "CFLAGS = %s" % get.CFLAGS())

def build():
    autotools.make("DESTDIR=%s prefix=/usr" % get.installDIR())

    # gitweb
    shelltools.unlink("gitweb/gitweb.cgi")
    autotools.make('GITWEB_CSS="gitweb/gitweb.css" \
                    GITWEB_LOGO="gitweb/git-logo.png" \
                    GITWEB_FAVICON="gitweb/git-favicon.png" \
                    bindir=/usr/bin \
                    gitweb/gitweb.cgi')

def install():
    autotools.rawInstall("DESTDIR=%s prefix=/usr" % get.installDIR())
    autotools.make("DESTDIR=%s prefix=/usr mandir=/usr/share/man install-doc" % get.installDIR())

    # Emacs stuff
    pisitools.insinto("/usr/share/emacs/site-lisp","contrib/emacs/*.el")

    # gitweb
    pisitools.insinto("/var/www/localhost/cgi-perl","gitweb/gitweb.cgi","gitweb.pl")
    pisitools.insinto("/var/www/localhost/cgi-perl/gitweb","gitweb/*.css")
    pisitools.insinto("/var/www/localhost/cgi-perl/gitweb","gitweb/*.png")

    perlmodules.fixLocalPod()

    pisitools.dodoc("README", "COPYING", "Documentation/SubmittingPatches")
