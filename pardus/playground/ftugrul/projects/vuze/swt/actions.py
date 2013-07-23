#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def setup():
    shelltools.makedirs("%s/src" % get.workDIR())
    shelltools.move("org", "%s/src/" % get.workDIR())
    pisitools.dosed("make_linux.mak", "AWT\_LIBS\ \=\ \-L\$\(AWT\_LIB\_PATH\)\ \-ljawt\ \-shared", "AWT_LIBS = -L$(AWT_LIB_PATH) -ljawt -shared -L/usr/lib/X11 -lX11")


def build():
    shelltools.export("MOZILLA_INCLUDES", "`pkg-config --cflags libxul libxul-embedding`")
    shelltools.export("MOZILLA_LIBS", "-Wl,-R`pkg-config libxul --variable=sdkdir` `pkg-config --libs libxul libxul-embedding`")
    shelltools.export("XULRUNNER_INCLUDES", "`pkg-config --cflags libxul libxul-embedding`")
    shelltools.export("XULRUNNER_LIBS", "-Wl,-R`pkg-config libxul --variable=sdkdir` `pkg-config --libs libxul libxul-embedding`")
    shelltools.export("AWT_LIB_PATH", "/opt/sun-jdk/jre/lib/i386")

    for target in ["awt", "swt", "atk", "gnome", "mozilla", "xulrunner", "cairo", "glx"]:
        autotools.make("-f make_linux.mak NO_STRIP=y CC=%s CXX=%s make_%s " % (get.CC(), get.CXX(), target))

    shelltools.system("ant compile")

    shelltools.copy("version.txt", "build")
    shelltools.copy("src/org/eclipse/swt/internal/SWTMessages.properties", "build/org/eclipse/swt/internal")

    shelltools.system("ant jar")

def install():
    pisitools.insinto("/usr/share/java", "swt.jar")
    pisitools.insinto("/usr/lib/jni", "*.so")

    pisitools.dodoc("about_files/*.txt")
    pisitools.dodoc("about_files/*README")
    pisitools.dohtml("about_files/*.html")
    pisitools.dohtml("*.html")
