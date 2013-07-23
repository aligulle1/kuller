#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    for dirs in ("nethack", "slashem"):
        autotools.make("%s/Makefile" % dirs)
        autotools.make("-C %s" % dirs)
        autotools.make("-C %s/util recover dlb dgn_comp lev_comp" % dirs)
        autotools.make("-C %s/dat spec_levs quest_levs" % dirs)

def install():
    autotools.make("-C nethack install \
                    GAMEDIR=%s/usr/share/vultureseye \
                    VARDIR=%s/var/lib/vultureseye \
                    SHELLDIR=%s/usr/bin"
                    % (get.installDIR(), get.installDIR(), get.installDIR()))

    autotools.make("-C slashem install \
                    GAMEDIR=%s/usr/share/vulturesclaw \
                    VARDIR=%s/var/lib/vulturesclaw \
                    SHELLDIR=%s/usr/bin"
                    % (get.installDIR(), get.installDIR(), get.installDIR()))

    for bin in ("vulturesclaw", "vultureseye"):
        pisitools.dosed("%s/usr/bin/%s" % (get.installDIR(), bin), get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "LICENSE")
