#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "Python-Docs-%s" % get.srcVERSION()
docdir = "/%s/%s/%s/html" % (get.docDIR(), get.srcNAME(), get.srcVERSION())

def install():
    pisitools.insinto(docdir, "*")

    pisitools.dodir("/etc/env.d")
    shelltools.echo("%s/etc/env.d/50python-docs" % get.installDIR(), "PYTHONDOCS=%s" % docdir)

