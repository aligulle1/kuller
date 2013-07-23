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

def setup():
    autotools.configure("--with-readline=gnu \
                         --enable-history-file \
                         --enable-rgip \
                         --enable-mgr \
                         --enable-iris \
                         --enable-thin-splines \
                         --with-x \
                         --x-includes=/usr/include/X11 \
                         --x-libraries=/usr/lib \
                         --with-linux-vga")

def build():
    autotools.make()

    # Docs
    shelltools.cd("docs")
    autotools.make("pdf")
    shelltools.cd("../tutorial")
    autotools.make("pdf")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Remove precompiled lisp files
    pisitools.remove("/usr/share/emacs/site-lisp/*.elc")

    # Docs, Demo, Manual and Tutorial files
    pisitools.insinto("/usr/share/doc/%s/demo" % get.srcTAG(), "demo/*")
    pisitools.remove("/usr/share/doc/%s/demo/Makefile*" % get.srcTAG())
    pisitools.insinto("/usr/share/doc/%s/manual" % get.srcTAG(), "docs/gnuplot.pdf")
    pisitools.insinto("/usr/share/doc/%s/tutorial" % get.srcTAG(), "tutorial/*.pdf")

    pisitools.dodoc("BUGS", "ChangeLog", "FAQ", "NEWS", "README*", "TODO")
