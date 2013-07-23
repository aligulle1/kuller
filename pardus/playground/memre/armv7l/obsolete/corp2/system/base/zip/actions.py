#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="."

def build():
    crosstools.make("-f unix/Makefile CC='%(CC)s' CPP='%(CPP)s' generic" % crosstools.environment)

def install():
    for bin in ["zip","zipcloak","zipnote","zipsplit"]:
        pisitools.dobin(bin)

    pisitools.doman("man/*.1")
    pisitools.dodoc("BUGS", "CHANGES", "MANUAL", "README", "TODO", "WHATSNEW", "WHERE")
