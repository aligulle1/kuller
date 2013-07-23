#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # plugins:
    # http://code.google.com/p/kate-pate-plugins
    # https://github.com/emyller/pate-plugins
    # http://www.muhuk.com/2008/11/extending-kate-with-pate
    # http://acim.name.tr/lp-dersler/ilkadimlar_KateLilyKDE.html
    cmaketools.configure()

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README*")
