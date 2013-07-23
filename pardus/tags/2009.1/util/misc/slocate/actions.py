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

def build():
    autotools.make()

def install():
    pisitools.dobin("src/slocate")

    # Uncomment for installing the cron script
    # pisitools.dobin("debian/cron.daily", "/etc/cron.daily")
    # pisitools.rename("/etc/cron.daily/cron.daily", "slocate")

    pisitools.doman("doc/*.1")
    pisitools.dodir("/var/lib/slocate")
    shelltools.touch("%s/var/lib/slocate/slocate.db" % get.installDIR())

    pisitools.dosym("slocate", "/usr/bin/locate")
    pisitools.dosym("slocate", "/usr/bin/updatedb")

    pisitools.dodoc("WISHLIST", "README", "Changelog", "notes")
