#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/gmailfs/", "gmailfs.py")
    pisitools.dobin("mount.gmailfs")

    pisitools.insinto("/etc", "gmailfs.conf")
