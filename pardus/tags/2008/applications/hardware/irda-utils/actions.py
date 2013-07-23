#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

D = {"target": get.installDIR(),
     "cflags": get.CFLAGS(),
     "docdir": "%s/%s" % (get.docDIR(), get.srcTAG())}

def build():
    shelltools.export("", get.CFLAGS())

    autotools.make('RPM_OPT_FLAGS="%(cflags)s" \
                    RPM_BUILD_ROOT="%(target)s" \
                    ROOT="%(target)s"' % D)

    shelltools.cd("irsockets")
    autotools.make("-j1")

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/sbin")

    autotools.install('PREFIX="%(target)s" \
                       ROOT="%(target)s" \
                       RPM_OPT_FLAGS="%(cflags)s" \
                       MANDIR="%(target)s/usr/share/man"' % D)

    pisitools.dodoc("README")
    pisitools.dodoc("etc/modules.conf.irda")
    pisitools.insinto(D["docdir"], "irsockets", "examples")

    # install README's into /usr/share/doc
    for i in ["irattach", "irdadump", "irdaping", "irsockets", "tekram"]:
        pisitools.newdoc(i + "/README", "README." + i)

    for i in ["irattach", "irdadump"]:
        pisitools.newdoc(i + "/ChangeLog", "ChangeLog." + i)

