#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"
Name = (get.srcVERSION()).replace(".","_")

def setup():
    shelltools.system("chmod +x construct.sh")
    shelltools.system("sh jdk-%s-dlj-linux-i586.bin --accept-license" % Name)

def install():
    pisitools.dodir("/opt")
    shelltools.system("./construct.sh . %s/opt/sun-jdk %s/opt/sun-jre"% (get.installDIR(),get.installDIR()))

    # Install mozilla plugin
    pisitools.dodir("/usr/lib/nsbrowser/plugins")
    pisitools.dosym("/opt/sun-jre/plugin/i386/ns7/libjavaplugin_oji.so", "/usr/lib/nsbrowser/plugins/javaplugin.so")

    for doc in ["COPYRIGHT", "LICENSE", "README.html", "THIRDPARTYLICENSEREADME.txt"]:
        file = "%s/opt/sun-jdk/%s" % (get.installDIR(),doc)
        pisitools.dodoc(file)
        shelltools.unlink(file)
