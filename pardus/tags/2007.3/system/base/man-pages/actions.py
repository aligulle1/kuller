#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    autotools.rawInstall("prefix=%s" % get.installDIR())
    pisitools.dodoc("man-pages-*.Announce", "README")

    # These come from coreutils
    pisitools.remove("/usr/share/man/man1/dir.1")
    pisitools.remove("/usr/share/man/man1/mv.1")
    pisitools.remove("/usr/share/man/man1/vdir.1")
    pisitools.remove("/usr/share/man/man1/mknod.1")
    pisitools.remove("/usr/share/man/man1/rm.1")
    pisitools.remove("/usr/share/man/man1/ls.1")
    pisitools.remove("/usr/share/man/man1/cp.1")
    pisitools.remove("/usr/share/man/man1/dircolors.1")
    pisitools.remove("/usr/share/man/man1/du.1")
    pisitools.remove("/usr/share/man/man1/install.1")
    pisitools.remove("/usr/share/man/man1/chgrp.1")
    pisitools.remove("/usr/share/man/man1/chmod.1")
    pisitools.remove("/usr/share/man/man1/rmdir.1")
    pisitools.remove("/usr/share/man/man1/mkdir.1")
    pisitools.remove("/usr/share/man/man1/ln.1")
    pisitools.remove("/usr/share/man/man1/df.1")
    pisitools.remove("/usr/share/man/man1/chown.1")
    pisitools.remove("/usr/share/man/man1/dd.1")
    pisitools.remove("/usr/share/man/man1/touch.1")
    pisitools.remove("/usr/share/man/man1/mkfifo.1")

    # These come from attr
    pisitools.remove("/usr/share/man/man2/flistxattr.2")
    pisitools.remove("/usr/share/man/man2/removexattr.2")
    pisitools.remove("/usr/share/man/man2/fgetxattr.2")
    pisitools.remove("/usr/share/man/man2/fsetxattr.2")
    pisitools.remove("/usr/share/man/man2/lsetxattr.2")
    pisitools.remove("/usr/share/man/man2/lremovexattr.2")
    pisitools.remove("/usr/share/man/man2/listxattr.2")
    pisitools.remove("/usr/share/man/man2/getxattr.2")
    pisitools.remove("/usr/share/man/man2/setxattr.2")
    pisitools.remove("/usr/share/man/man2/llistxattr.2")
    pisitools.remove("/usr/share/man/man2/fremovexattr.2")
    pisitools.remove("/usr/share/man/man2/lgetxattr.2")

    # Comes from xorg-input
    pisitools.remove("/usr/share/man/man4/mouse.4")
