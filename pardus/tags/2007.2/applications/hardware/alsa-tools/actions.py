#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


alsa_tools = ["ac3dec","envy24control","rmedigicontrol","hdsploader", "mixartloader","vxloader",
              "usx2yloader","sscape_ctl","sb16_csp","as10k1","ld10k1", "us428control"]

docs = ["README","ChangeLog"]


def setup():
    for tool in alsa_tools:
        shelltools.cd(tool)
        autotools.configure("--with-gtk2")
        shelltools.cd("..")

def build():
    for tool in alsa_tools:
        shelltools.cd(tool)
        autotools.make()
        shelltools.cd("..")

def install():
    for tool in alsa_tools:
        shelltools.cd(tool)
        autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())

        for doc in docs:
            pisitools.insinto("/usr/share/doc/%s/%s" % (get.srcTAG(),tool), doc)

        shelltools.cd("..")
