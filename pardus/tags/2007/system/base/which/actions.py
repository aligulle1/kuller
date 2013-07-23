#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()
    
def build():
    autotools.make()
    
def install():
    pisitools.dobin("which")
    pisitools.doman("which.1")
    pisitools.doinfo("which.info")
