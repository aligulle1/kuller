#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static")

def build():
    autotools.make("install_doc_dir=/usr/share/doc/%s all" % get.installDIR())

def install():
    autotools.rawInstall("DESTDIR=%s INST_LIB_DIR=%s/usr/lib" % (get.installDIR(),get.installDIR()))
