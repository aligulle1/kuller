#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-gc=system")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move for working
    pisitools.domove("/usr/share/asymptote/*.el", "/usr/share/emacs/site-lisp/")
    pisitools.domove("/usr/share/asymptote/*.vim","/usr/share/vim/vim70/asy/")
    pisitools.domove("/usr/share/asymptote/*.py","/usr/lib/python2.4/site-packages/")

    # remove xasy and xasy.1x
    pisitools.remove("/usr/bin/xasy")
    pisitools.remove("/usr/share/man/man1/xasy.1x")
