#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools

WorkDir="libintl-perl-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.dodoc("ChangeLog", "COPYING.LESSER", "FAQ", "MANIFEST", "NEWS", "README", "README-oldversions", "THANKS", "TODO")