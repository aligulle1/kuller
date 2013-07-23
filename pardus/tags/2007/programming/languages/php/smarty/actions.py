#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def setup():
    pass

def build():
    pass

def install():
    pisitools.insinto("/usr/share/php5/smarty/", "libs/*")
    pisitools.insinto("/usr/share/php5/smarty/", "misc/smarty_icon.gif", "smarty.gif")
    pisitools.dodoc("BUGS", "ChangeLog", "COPYING.lib", "FAQ", "NEWS", "QUICK_START", "README", \
                    "RELEASE_NOTES", "TODO")
