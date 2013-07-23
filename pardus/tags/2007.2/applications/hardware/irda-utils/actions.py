#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "irda-utils-0.9.17"

def build():
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.export("WANT_AUTOMAKE", "1.4")
    shelltools.export("RPM_OPT_FLAGS", get.CFLAGS())

    autotools.make('ROOT="%s" RPM_BUILD_ROOT="%s"' % (get.installDIR(), get.installDIR()))

    shelltools.cd("irsockets")
    autotools.make()

def install():
    pisitools.dodir("/usr/bin")
    pisitools.dodir("/usr/sbin")

    autotools.install('PREFIX="%(D)s" ROOT="%(D)s" MANDIR="%(D)s/usr/share/man"' % {"D": get.installDIR()})

    pisitools.dobin("irsockets/irdaspray")
    pisitools.dobin("irsockets/ias_query")
    pisitools.dobin("irsockets/irprintf")
    pisitools.dobin("irsockets/irprintfx")
    pisitools.dobin("irsockets/irscanf")
    pisitools.dobin("irsockets/recv_ultra")
    pisitools.dobin("irsockets/send_ultra")

    pisitools.dodoc("README")
    pisitools.dodoc("etc/modules.conf.irda")

    # install README's into /usr/share/doc
    for i in ["irattach", "irdadump", "irdaping", "irsockets", "tekram"]:
        pisitools.newdoc(i + "/README", "README." + i)
