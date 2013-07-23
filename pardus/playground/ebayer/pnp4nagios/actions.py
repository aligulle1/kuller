#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#WorkDir = ""

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("sample-config/httpd.conf.in", "AuthUserFile /usr/local/nagios/etc/htpasswd.users", "AuthUserFile /etc/nagios/htpasswd.users")
    autotools.configure("--with-nagios-user=nagios \
                         --with-nagios-group=nagios \
                         --bindir=/usr/sbin \
                         --libexecdir=/usr/libexec/pnp4nagios \
                         --sysconfdir=/etc/pnp4nagios \
                         --localstatedir=/var/log/pnp4nagios \
                         --datadir=/usr/share/pnp4nagios \
                         --datarootdir=/usr/share/pnp4nagios \
                         --with-perfdata-dir=/var/lib/pnp4nagios/perfdata \
                         --with-perfdata-logfile=/var/log/pnp4nagios/perfdata.log \
                         --with-perfdata-spool-dir=/var/spool/pnp4nagios")

def build():
    autotools.make("all")

def install():
    pisitools.dodir("/etc/apache2/conf.d")
    # autotools.make("DESTDIR=%s install install-webconf" % get.installDIR())
    autotools.make("DESTDIR=%s fullinstall" % get.installDIR())
    pisitools.removeDir("/etc/init.d")

    # remove unnecessary files
    pisitools.remove("/usr/share/pnp4nagios/install.php")

    # move docs and sample-configs into docdir
    # pisitools.dodir("/usr/share/doc/pnp4nagios")
    # pisitools.move("%s/etc/pnp4nagios/background.pdf" % get.installDIR(), "%s/usr/share/doc/pnp4nagios/" % get.installDIR())
    # pisitools.move("%s/etc/pnp4nagios/pnp4nagios_release" % get.installDIR(), "%s/usr/share/doc/pnp4nagios/" % get.installDIR())
    # pisitools.dodoc("sample-config/*-sample", "sample-config/pnp/*-sample", "sample-config/pnp/check_commands", "sample-config/pnp/pages")
    # pisitools.insinto("/etc/pnp4nagios", "sample-config/pnp/npcd.cfg-sample", "npcd.cfg")
