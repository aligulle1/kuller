#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "Gtk2-Ex-FormFactory-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
    shelltools.system("cp -Rv ./examples /usr/share/doc/perl-Gtk2-Ex-FormFactory-%s" % get.srcVERSION())
    shelltools.system("cp -Rv ./tutorial /usr/share/doc/perl-Gtk2-Ex-FormFactory-%s" % get.srcVERSION())
    pisitools.dodoc("Changes", "LICENSE", "README")