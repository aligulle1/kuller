#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.autoconf()
    autotools.configure("--with-emacs=emacs \
                         --with-icondir=/%s/usr/share/emacs/23.0.94/etc/images/w3m" %  get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()
    autotools.install("install-icons")

    pisitools.remove("/usr/share/emacs/site-lisp/w3m/*.elc")

    pisitools.dodoc("COPYING", "README", "NEWS", "ChangeLog")
