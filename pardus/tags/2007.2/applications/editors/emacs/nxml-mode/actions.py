#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="nxml-mode-%s" % get.srcVERSION().split('_')[-1]

def install():
    for data in ["*.el","schema"]:
        pisitools.insinto("/usr/share/emacs/site-lisp", data)

    pisitools.doinfo("nxml-mode.info")
