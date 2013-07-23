#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = get.srcNAME()

def setup():
    autotools.configure("--with-checkresult-dir=/var/spool/nagios/checkresults \
                         --with-lockfile=/var/run/nagios/nagios.lock \
                         --with-nagios-user=nagios \
                         --with-nagios-group=nagios \
                         --with-command-group=nagioscmd \
                         --with-mail=/usr/sbin/sendmail \
                         --with-template-objects \
                         --with-template-extinfo \
                         --with-event-broker \
                         --with-perlcache \
                         --enable-embedded-perl \
                         --localstatedir=/var/log/nagios \
                         --datadir=/usr/share/nagios/html \
                         --sysconfdir=/etc/nagios \
                         --libexecdir=/usr/lib/nagios/plugins STRIP=/bin/true")

def build():
    autotools.make("DESTDIR=%s CGIDIR=/%s/nagios/cgi-bin all" % (get.installDIR(), get.dataDIR()))

def install():
    autotools.make("DESTDIR=%s COMMAND_OPTS=\"\" INSTALL_OPTS=\"\" INIT_OPTS=\"\" CGIDIR=/%s/nagios/cgi-bin STRIP=/bin/true install install-commandmode install-config" % (get.installDIR(), get.dataDIR()))

    config_dirs = ["servers", "printers", "switches", "routers", "conf.d", "plugins.d"]
    for d in config_dirs:
        pisitools.dodir("/etc/nagios/%s" %d)

    pisitools.dodir("/var/run/nagios")
    pisitools.dodir("/usr/lib/nagios/plugins")
    pisitools.dodir("/usr/lib/nagios/plugins/eventhandlers")

