#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # hmmm, we should do the hal mounting with gnome-mount?
    pisitools.dosed("configure.in", r"(ac_cv_func_posix_getpwuid_r=)\w*", "\\1yes")
    autotools.autoreconf("-fi")

    cache = [ "ac_cv_func_posix_getpwuid_r=yes", ]
    autotools.configure("--enable-ipv6 \
                         --enable-hal \
                         --disable-samba \
                         --disable-krb5 \
                         --enable-avahi \
                         --enable-acl \
                         --disable-selinux \
                         --disable-static \
                         --disable-schemas-install \
                         --disable-cdda \
                         --disable-fam \
                         --disable-howl \
                         --with-hal-mount=/usr/bin/mount \
                         --with-hal-umount=/usr/bin/umount \
                         --with-hal-eject=/usr/bin/eject", cache=cache)
                         # FIXME:
                         # --enable-samba
                         # --enable-krb5

def build():
    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("TODO", "NEWS", "README", "HACKING", "AUTHORS", "ChangeLog")
