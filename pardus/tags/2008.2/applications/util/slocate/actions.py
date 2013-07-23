#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
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
    pisitools.newman("doc/slocate.1", "/usr/share/man/man1/slocate.1")

    pisitools.dodir("/var/lib/slocate")
    shelltools.touch("%s/var/lib/slocate/slocate.db" % get.installDIR())

    pisitools.dosym("slocate", "/usr/bin/locate")
    pisitools.dosym("slocate", "/usr/bin/updatedb")
    pisitools.dosym("slocate.1.gz", "/usr/share/man/man1/locate.1.gz")

    pisitools.dodoc("AUTHORS", "README", "ChangeLog")
