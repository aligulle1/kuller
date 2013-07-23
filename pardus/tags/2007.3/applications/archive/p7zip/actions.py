#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "p7zip_4.43"

def setup():
    pisitools.dosed('install.sh','DEST_HOME=/usr/local','DEST_HOME=/usr')
    pisitools.dosed('install.sh','DEST_DIR=','DEST_DIR=%s' % get.installDIR())
    pisitools.dosed('install.sh','DEST_MAN=\${DEST_HOME}/man','DEST_MAN=${DEST_HOME}/share/man')

def build():
    autotools.make("OPTFLAGS=\"%s\" all2" % get.CFLAGS())

def install():
    shelltools.system("./install.sh")

    pisitools.dodoc("ChangeLog", "README", "TODO", "DOCS/*.txt")
    pisitools.dohtml("DOCS/MANUAL/*")

