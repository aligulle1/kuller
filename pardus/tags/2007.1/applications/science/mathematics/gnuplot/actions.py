#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "gnuplot-4.2.rc1"

def setup():
    autotools.configure("--with-readline=gnu \
                         --enable-history-file \
                         --enable-rgip \
                         --enable-mgr \
                         --enable-iris \
                         --enable-thin-splines \
                         --disable-wxwidgets \
                         --with-x \
                         --x-includes=/usr/include/X11 \
                         --x-libraries=/usr/lib \
                         --with-linux-vga")

def build():
    autotools.make()

    # docs
    shelltools.cd("docs")
    autotools.make("pdf")
    shelltools.cd("../tutorial")
    autotools.make("pdf")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Docs, Demo, Manual and Tutorial files
    pisitools.insinto("/usr/share/doc/%s/demo" % get.srcTAG(), "demo/*")
    pisitools.remove("/usr/share/doc/%s/demo/Makefile*" % get.srcTAG())
    pisitools.remove("/usr/share/texmf-local/tex/latex/gnuplot/gnuplot.cfg")
    pisitools.insinto("/usr/share/doc/%s/manual" % get.srcTAG(), "docs/gnuplot.pdf")
    pisitools.insinto("/usr/share/doc/%s/tutorial" % get.srcTAG(), "tutorial/*.pdf")
    pisitools.insinto("/usr/share/doc/%s/psdoc" % get.srcTAG(), "docs/psdoc/*.doc")
    pisitools.insinto("/usr/share/doc/%s/psdoc" % get.srcTAG(), "docs/psdoc/*.ps")
    pisitools.insinto("/usr/share/doc/%s/psdoc" % get.srcTAG(), "docs/psdoc/*.gpi")
    pisitools.dodoc("BUGS", "ChangeLog", "FAQ", "NEWS", "PATCHLEVEL", "PGPKEYS", "PORTING", "README*", "TODO", "VERSION")
