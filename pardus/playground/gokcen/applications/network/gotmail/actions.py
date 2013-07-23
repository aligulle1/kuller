#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.dobin("gotmail")
    pisitools.insinto("%s/man1/" % get.manDIR(), "gotmail.1.gz")
    pisitools.dodir("/usr/share/gotmail")
    pisitools.insinto("/usr/share/gotmail/", "sample.gotmailrc")

    pisitools.dodoc("README", "VERSION", "ChangeLog")
