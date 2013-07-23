#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--enable-bonobo-activation-debug=yes \
                         --disable-static", predefinedVars="ORBIT_IDL=`which orbit-idl-2`")
    pisitools.dosed("libtool"," -shared "," -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("TODO", "NEWS", "README", "ChangeLog", "AUTHORS")
