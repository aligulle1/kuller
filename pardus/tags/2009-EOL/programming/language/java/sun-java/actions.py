#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"
Name = "6u26"

def setup():
    shelltools.system("sh jdk-%s-dlj-linux-i586.bin --accept-license" % Name)

def install():
    pisitools.dodir("/opt")
    shelltools.system("./construct . %s/opt/sun-jdk %s/opt/sun-jre"% (get.installDIR(),get.installDIR()))

    pisitools.dodir("/usr/lib/nsbrowser/plugins")

    # Next generation Java plugin is needed by Firefox 3.6+
    # http://java.sun.com/javase/6/webnotes/install/jre/manual-plugin-install-linux.html
    pisitools.dosym("/opt/sun-jre/lib/i386/libnpjp2.so", "/usr/lib/nsbrowser/plugins/javaplugin_new.so")

    # Keep old Firefox plugin for backwards compatibility
    pisitools.dosym("/opt/sun-jre/plugin/i386/ns7/libjavaplugin_oji.so", "/usr/lib/nsbrowser/plugins/javaplugin.so")

    for doc in ["COPYRIGHT", "LICENSE", "README.html", "THIRDPARTYLICENSEREADME.txt"]:
        file = "%s/opt/sun-jdk/%s" % (get.installDIR(), doc)
        pisitools.dodoc(file)
        shelltools.unlink(file)
