#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

console_tools = ["ac3dec", "hdsploader",
                 "mixartloader", "vxloader",
                 "usx2yloader", "sscape_ctl",
                 "sb16_csp", "as10k1", "ld10k1",
                 "us428control", "seq/sbiload"]

gui_tools = ["envy24control", "rmedigicontrol", "hdspconf",
             "hdspmixer", "echomixer", "qlo10k1"]

alsa_tools = gui_tools + console_tools

docs = ["README", "ChangeLog", "AUTHORS", "COPYING", "NEWS", "TODO"]

def setup():
    for tool in alsa_tools:
        shelltools.cd(tool)
        autotools.configure()
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
            if tool in gui_tools:
                srctag = "alsa-tools-gui-%s-%s" % (get.srcVERSION(), get.srcRELEASE())
            else:
                srctag = get.srcTAG()

            pisitools.insinto("/usr/share/doc/%s/%s" % (srctag, tool), doc)

        shelltools.cd("..")

    pisitools.remove("/usr/share/applications/hdspmixer.desktop")
    pisitools.remove("/usr/share/applications/hdspconf.desktop")
