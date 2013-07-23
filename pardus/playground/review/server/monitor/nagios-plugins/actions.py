#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--localstatedir=/var/log/nagios \
                         --sysconfdir=/etc/nagios \
                         --libexecdir=/usr/lib/nagios/plugins \
                         --enable-extra-opts \
                         --disable-static \
                         --disable-rpath \
                         --with-ps-varlist='procstat,&procuid,&procpid,&procppid,&procvsz,&procrss,&procpcpu,procetime,procprog,&pos' \
                         --with-ps-command=\"/bin/ps -eo 's uid pid ppid vsz rss pcpu etime comm args'\" \
                         --with-ps-format='%s %d %d %d %d %d %f %s %s %n' \
                         --with-ps-cols=10 \
                         --with-ipv6 \
                         --with-openssl=/usr \
                         --with-msql=/usr \
                         --with-pgsql=/usr \
                         --with-nagios-user=nagios \
                         --with-nagios-group=nagios")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/nagios-plugins", "contrib")
    pisitools.insinto("/etc/nagios/plugins.d", "command.cfg", "command.cfg.do_not_use")

    pisitools.removeDir("/usr/include")
    pisitools.remove("/usr/lib/nagios/plugins/check_apt")

    pisitools.dodoc("ABOUT-NLS", "ACKNOWLEDGEMENTS", "AUTHORS", "BUGS", "ChangeLog", "CODING", "COPYING", "FAQ", "LEGAL", "NEWS", "README", "REQUIREMENTS", "SUPPORT", "THANKS")
