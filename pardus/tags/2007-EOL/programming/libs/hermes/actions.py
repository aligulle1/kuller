#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get 

WorkDir = "Hermes-1.3.3"

def dadocfunc(_from, _to):
    _dir = "/usr/share/doc/%s/%s" % (get.srcTAG(), _to)
    pisitools.dodir(_dir)
    pisitools.insinto(_dir, _from)

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.8")
    shelltools.export("WANT_AUTOCONF", "2.5")

    libtools.libtoolize("--force --copy")
    autotools.aclocal()
    autotools.automake("-a -f -c")
    autotools.autoconf()

    autotools.configure("--with-pic")
    
    # for future reference
    #                     --disable-x86asm")

def build():
    autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"' % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ", "NEWS", "README", "TODO*")

    pisitools.dohtml("docs/api/*")

    dadocfunc("docs/api/*.ps", "print")
    dadocfunc("docs/api/*.txt", "txt")
    dadocfunc("docs/api/sgml/*.sgml", "sgml")

