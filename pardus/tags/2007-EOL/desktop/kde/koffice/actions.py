#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("kugar/kudesigner/kudesigner.desktop", "^Icon=kudesigner", "Icon=kugar")
    pisitools.dosed("tools/kthesaurus/KThesaurus.desktop", "^Icon=kthesaurus", "Icon=kdict")

    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
