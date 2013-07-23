#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "PolicyKit-0.2_CVS_20060725"

def setup():
    autotools.autoreconf()
    autotools.configure("--with-pam-module-dir=/lib/security/ \
                         --with-os-type=Pardus \
                         --with-polkit-user=polkit \
                         --with-polkit-group=polkit \
                         --with-pid-file=/var/run/PolicyKit/pid \
                         --disable-docbook-docs \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s/" % get.installDIR())

    pisitools.dodir("/var/run/PolicyKit")
