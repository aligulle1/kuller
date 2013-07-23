#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/php5/smarty/", "libs/*")
    pisitools.insinto("/usr/share/php5/smarty/", "misc/smarty_icon.gif", "smarty.gif")

    pisitools.dodoc("BUGS", "ChangeLog", "COPYING.lib", "FAQ", "NEWS", "QUICK_START", "README", "RELEASE_NOTES", "TODO")
