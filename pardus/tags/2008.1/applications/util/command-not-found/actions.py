#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "command-not-found-0.2"

def build():
    pass

def install():
    pisitools.dobin("src/command-not-found")
    pisitools.insinto("/var/command-not-found", "data/packages.db")

    for lang in ["de", "es", "fr", "it", "nl", "pl", "tr"]:
        pisitools.domo("po/%s.po" % lang, lang, "command-not-found.mo")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
