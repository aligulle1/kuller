#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --localstatedir=/var \
                            --sysconfdir=/etc \
                            --enable-static=no \
                            --with-wwwroot=/var/www/localhost/cherokee \
                            --with-wwwuser=apache \
                            --with-wwwgroup=apache \
                            --enable-os-string='Pardus Linux'")

    pisitools.dosed("cherokee.conf.sample.pre", "log/", "log/cherokee/")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/etc/pam.d", "pam.d_cherokee", "cherokee")

    #Contrib scripts
    pisitools.insinto("/usr/share/cherokee", "contrib")
    pisitools.remove("/usr/share/cherokee/contrib/Makefile*")
    pisitools.remove("/usr/share/cherokee/contrib/cherokee")

    #Docs
    pisitools.dohtml("%s/usr/share/doc/cherokee/media" % get.installDIR())
    pisitools.dohtml("%s/usr/share/doc/cherokee/*.html" % get.installDIR())
    pisitools.removeDir("/usr/share/doc/cherokee/media")
    pisitools.remove("/usr/share/doc/cherokee/*.html")
    pisitools.dodoc("README", "ChangeLog", "AUTHORS")

