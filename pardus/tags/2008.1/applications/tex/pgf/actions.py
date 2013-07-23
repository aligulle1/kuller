# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    target = "/usr/share/texmf-dist/tex/"
    pisitools.dodir(target)

    pisitools.insinto(target, "latex")
    pisitools.insinto(target, "generic")
    pisitools.insinto(target, "plain")

    pisitools.dodoc("README")
