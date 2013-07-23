#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

WorkDir = "Ocsinventory-Agent-1.1.2"

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import perlmodules

def build():
    shelltools.system("/usr/bin/perl Makefile.PL INSTALLDIRS=vendor")
    autotools.make()

def install():
    # autotools.rawInstall("DESTDIR=%s PREFIX=/%s" % (get.installDIR(), get.defaultprefixDIR()))
    autotools.make("pure_install DESTDIR=%s PREFIX=/%s" % (get.installDIR(), get.defaultprefixDIR()))
    # pisitools.move("%s/ocsinventory-agent" % get.binDIR(), "%s/ocsinventory-agent" % get.sbinDIR())
    pisitools.dodir("/var/log/ocsinventory-agent")
    pisitools.dodir("/var/lib/ocsinventory-agent")
    # pisitools.dodir("%s/logrotate.d" % get.confDIR())
    # pisitools.dodir("%s/cron.hourly" % get.confDIR())
    # pisitools.dodir("%s/ocsinventory/ocsinventory-agent" % get.confDIR())
    pisitools.insinto("%s/" % get.confDIR(), "etc/*")
