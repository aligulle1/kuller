#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("-with-init-script=none \
                        --with-qemud-pid-file=/var/run/libvirt_qemud.pid \
                        --with-remote-file=/var/run/libvirtd.pid \
                        --localstatedir=/var \
                        --with-xen-proxy=yes")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gtk-doc/html")
    pisitools.dodoc("AUTHORS", "NEWS", "README*", "ChangeLog")
