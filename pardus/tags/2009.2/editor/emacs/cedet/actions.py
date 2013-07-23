#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
import os

WorkDir='cedet-%s' % get.srcVERSION().replace('_','')

def build():
    autotools.make("-j1")

def install():
    folders = ['cogre', 'common', 'contrib', 'ede', 'eieio', 'semantic', 'speedbar']
    for folder in folders:
        pisitools.insinto('/usr/share/emacs/site-lisp/cedet/', folder)

    for root, dirs, files in os.walk(get.workDIR()):
        for name in files:
            f = os.path.join(root, name)
            if f.endswith("info"):
                pisitools.doinfo(f)

    remove = ['AUTHORS', 'ONEWS', 'README', 'NEWS', 'INSTALL', 'Makefile', 'Project.ede', 'ChangeLog']

    for root, dirs, files in os.walk("%s/usr/share/emacs/site-lisp/cedet/" % get.installDIR()):
        for name in files:
            if name in remove:
                shelltools.unlink(os.path.join(root, name))
            elif name.split(".")[-1] in ("info", "info-1", "info-2", "info-3", "info-4", "~", "~1~", "el~", "elc", "texi"):
                shelltools.unlink(os.path.join(root, name))
