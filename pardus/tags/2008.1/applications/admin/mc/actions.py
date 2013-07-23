#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "mc-4.6.2-pre1"

def setup():
    shelltools.export("CFLAGS", "%s -DUTF8 -I/usr/include/gssapi" % get.CFLAGS())
    shelltools.move("po/no.po",  "po/nb.po")
    shelltools.move("po/no.gmo", "po/nb.gmo")
    shelltools.unlink("po/tr.gmo")

    autotools.configure("--with-screen=slang \
                         --with-gpm-mouse \
                         --with-included-gettext \
                         --with-vfs \
                         --with-ext2undel \
                         --with-edit \
                         --with-x=yes \
                         --enable-charset \
                         --with-samba \
                         --with-configdir=/etc/samba \
                         --with-codepagedir=/var/lib/samba/codepages \
                         --with-privatedir=/etc/samba/private")

def build():
    shelltools.export("CFLAGS", "%s -I/usr/include/gssapi" % get.CFLAGS())
    autotools.make()
    shelltools.cd("po")
    autotools.make("tr.gmo")

def install():
    autotools.install()
    pisitools.dodoc("ChangeLog", "AUTHORS", "MAINTAINERS", "FAQ", "NEWS", "README*")

    # Do not mess with glibc files
    pisitools.remove("/usr/share/locale/locale.alias")

    # Do not carry empty dirs
    pisitools.removeDir("/usr/sbin")
    pisitools.removeDir("/usr/share/man/man8")
