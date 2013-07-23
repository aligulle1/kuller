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

NoStrip = "/"
WorkDir = "alsa-driver"

def setup():
    autotools.configure("--with-oss \
                         --with-kernel=/lib/modules/%s/source \
                         --with-isapnp=yes \
                         --with-sequencer=yes \
                         --with-card-options=all \
                         --with-cards=all" % get.curKERNEL())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-modules")

    # These will be updated after modules are installed, they shouldn't be
    # included in the package itself
    pisitools.remove("/lib/modules/*/modules.*")

    for f in shelltools.ls("alsa-kernel/Documentation/*txt"):
        pisitools.dodoc(f)
    pisitools.dodoc("doc/serialmidi.txt")
