#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.rename("/usr/kde/3.5/share/locale/de/LC_MESSAGES/tmp.mo", "klogic.mo")
    pisitools.rename("/usr/kde/3.5/share/locale/es/LC_MESSAGES/tmp.mo", "klogic.mo")
    pisitools.rename("/usr/kde/3.5/share/locale/fr/LC_MESSAGES/tmp.mo", "klogic.mo")
    pisitools.rename("/usr/kde/3.5/share/locale/it/LC_MESSAGES/tmp.mo", "klogic.mo")
    pisitools.rename("/usr/kde/3.5/share/locale/sv/LC_MESSAGES/tmp.mo", "klogic.mo")
    pisitools.rename("/usr/kde/3.5/share/locale/tr/LC_MESSAGES/tmp.mo", "klogic.mo")
