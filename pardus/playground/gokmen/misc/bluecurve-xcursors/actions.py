#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir="redhat-cursors"

def install():
    for theme in ['Bluecurve-FC4','Bluecurve-FC6','Bluecurve-inverse-FC4','Bluecurve-inverse-FC6']:
        pisitools.insinto("/usr/share/icons", theme)
    pisitools.dodoc("README")

