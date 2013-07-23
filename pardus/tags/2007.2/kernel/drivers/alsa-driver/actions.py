#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = "/"

def setup():
    autotools.configure("--with-oss \
                         --with-kernel=/usr/src/linux \
                         --with-isapnp=yes \
                         --with-sequencer=yes \
                         --with-cards=all")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-modules")

    # These will be updated after modules are installed, they souldn't be
    # included in the package itself
    pisitools.remove("/lib/modules/*/modules.*")

    for f in shelltools.ls("alsa-kernel/Documentation/*txt"):
        pisitools.dodoc(f)
    pisitools.dodoc("doc/serialmidi.txt")
