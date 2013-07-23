#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

from pisi.actionsapi import kerneltools

NoStrip = "/"

if "_" in get.srcVERSION():
    # Snapshot
    WorkDir = "alsa-driver"
else:
    # Upstream tarball
    WorkDir = "alsa-driver-%s" % get.srcVERSION()

def setup():
    autotools.configure("--with-oss \
                         --with-kernel=/lib/modules/%s/build \
                         --with-isapnp=yes \
                         --with-sequencer=yes \
                         --with-card-options=all \
                         --disable-verbose-printk \
                         --with-cards=all" % kerneltools.getKernelVersion())
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-modules")

    for f in shelltools.ls("alsa-kernel/Documentation/*txt"):
        pisitools.dodoc(f)

    pisitools.dodoc("doc/serialmidi.txt")
