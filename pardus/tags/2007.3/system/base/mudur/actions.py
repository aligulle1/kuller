#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    shelltools.system("./setup.py install %s" % get.installDIR())
