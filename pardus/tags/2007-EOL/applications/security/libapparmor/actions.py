#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.
#
# S.Çağlar Onur <caglar@pardus.org.tr> 

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "libapparmor-2.0"

def setup():
    pisitools.dosed("Makefile", "include Make.rules")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s LIB=/lib VERSION=2 RELEASE=6288" % get.installDIR())
