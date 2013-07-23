#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("Makefile", r"(^CC\s*=)\s*gcc\s*(.*)$", "\\1 %(CC)s %(CFLAGS)s \\2" % crosstools.environment)
    pisitools.dosed("Makefile", r"(^LDFLAGS\s*=)\s*(.*)$", "\\1 %(LDFLAGS)s \\2 -Wl,-z,now" % crosstools.environment)

def build():
    crosstools.make()

def install():
    pisitools.doman("crontab.1", "crontab.5", "cron.8")
    pisitools.dodoc("CHANGES", "CONVERSION", "FEATURES", "MAIL", "README", "THANKS")

    pisitools.dosbin("cron")
    pisitools.dobin("crontab")

    pisitools.dodir("/var/spool/cron/crontabs")
    pisitools.dodir("/etc/cron.d")
