#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    autotools.autoreconf("-fvi")
    autotools.configure("-with-init-script=none \
                        --with-remote-pid-file=/var/run/libvirtd.pid \
                        --localstatedir=/var \
                        --without-xen-proxy --without-xen \
                        --without-vbox \
                        --with-qemu \
                        --without-openvz \
                        --without-lxc \
                        --without-uml \
                        --with-sasl \
                        --with-avahi \
                        --with-polkit \
                        --with-network \
                        --without-storage-lvm \
                        --without-storage-iscsi \
                        --without-selinux \
                        --with-hal \
                        --without-driver-modules \
                        --disable-iptables-lokkit \
                        --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gtk-doc/html")
    pisitools.dodoc("AUTHORS", "NEWS", "README*", "ChangeLog")
