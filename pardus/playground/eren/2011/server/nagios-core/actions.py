#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "nagios-%s" % get.srcVERSION()

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --bindir=/usr/sbin \
                            --sbindir=/usr/lib/nagios/cgi-bin \
                            --libexecdir=/usr/lib/nagios/plugins \
                            --datadir=/usr/share/nagios/htdocs \
                            --localstatedir=/var/nagios \
                            --with-checkresult-dir=/var/nagios/spool/checkresults \
                            --sysconfdir=/etc/nagios \
                            --enable-embedded-perl \
                            --with-nagios-user=root \
                            --with-nagios-group=root \
                            --with-command-user=nagios \
                            --with-command-group=nagios \
                            --with-httpd-conf=/etc/apache2/conf.d \
                            --with-lockfile=/var/run/nagios.lock \
                            --enable-DEBUG0 \
                            --enable-DEBUG1 \
                            --enable-DEBUG2 \
                            --enable-DEBUG3 \
                            --enable-DEBUG4 \
                            --enable-DEBUG5")

def build():
    autotools.make("all")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    autotools.rawInstall("DESTDIR=%s install-config" % get.installDIR())

    pisitools.dodir("/var/nagios/rw")

    pisitools.dodoc("README", "Changelog")
