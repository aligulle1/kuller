#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    crosstools.configure("--enable-color \
                          --enable-nanorc \
                          --enable-utf8 \
                          --disable-speller")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("program_transform_name= DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/etc/", "doc/nanorc.sample", "nanorc")
    pisitools.dosym("/usr/bin/nano", "/bin/nano")

    pisitools.dohtml("doc/*.html")
    pisitools.dodoc("ChangeLog*", "README", "doc/nanorc.sample", "AUTHORS", "BUGS", "NEWS", "TODO", "COPYING*", "THANKS", "UPGRADE")
