#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.system('/usr/sbin/apxs2 -c mod_fastcgi.c fcgi*.c')

def install():
    pisitools.insinto('/usr/lib/apache2/modules', '.libs/mod_fastcgi.so')
