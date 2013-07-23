#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="plt"

def setup():
    shelltools.cd("src/")
    autotools.configure("--enable-mred \
                        --enable-perl \
                        --enable-gl \
                        --enable-libpng \
                        --enable-libjpeg \
                        --enable-cairo \
                        --prefix=/usr/share/drscheme")

def build():
    shelltools.cd("src/")
    autotools.make()

def install():
    shelltools.cd("src/")
    pisitools.dosed("Makefile", "cp -p", "cp")

    pisitools.dodir("/usr/share/drscheme")
    
    autotools.install("prefix=%s/usr/share/drscheme" % get.installDIR())
    
    pisitools.dodoc("README")
    
    shelltools.cd("%s/usr/share/drscheme/man/man1" % get.installDIR())
    pisitools.doman("*")
    pisitools.removeDir("/usr/share/drscheme/man")

    executableList = ["mzc", "web-server", "web-server-monitor", "web-server-text", "tex2page", "help-desk", "drscheme", "setup-plt"]

    for executable in executableList:
        target = "%s/usr/share/drscheme/bin/%s" % (get.installDIR(), executable)
        pisitools.dosed(target, "%s/usr/share/drscheme" % get.installDIR(), "/usr/share/drscheme")
        shelltools.chmod(target)
        pisitools.dosym("/usr/share/drscheme/bin/%s" % executable, "/usr/bin/%s" % executable)

    # list of scripts/files has PLT_HOME=/var/tmp/pisi/drscheme-3.0.1-1/install/usr/share/drscheme defined
    sedList =["bin/framework-test", "bin/framework-test-engine", "bin/games", \
                "bin/gmzc", "bin/mzpp", "bin/mztext", "bin/pdf-slatex", "bin/planet", \
                "bin/slatex", "bin/slideshow", "bin/swindle", "collects/info-domain/compiled/cache.ss"]

    # remove /var/tmp/pisi/drscheme-3.0.1-1/install prefix
    # FIXME: convert to dosed
    for executable in sedList:
        shelltools.system("sed -i -e 's~/var/tmp/pisi/%s/install~~g' %s/usr/share/drscheme/%s" % (get.srcTAG(), get.installDIR(), executable))

