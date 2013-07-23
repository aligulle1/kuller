#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "foomatic-filters-ppds-%s" % get.srcVERSION().split("_", 1)[1]
NoStrip = "/"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if "gimp-print" in name or "hpijs" in name:
                shelltools.unlink(os.path.join(root, name))

def setup():
    # not to conflict with gutenprint and hpijs,  package is cleaned with
    # rm -f `find . -name "*gimp-print*" `
    # rm -f `find . -name "*hpijs*" `
    fixperms("share/ppd")

def install():
    shelltools.system("./install -d %s -p /usr -z" % get.installDIR())
    pisitools.dodir("/usr/share/cups/model")
    pisitools.dosym("/usr/share/ppd", "/usr/share/cups/model/foomatic-ppds")

    # not to conflict with foomatic-filters
    pisitools.removeDir("/usr/bin")
    pisitools.removeDir("/usr/share/man")
