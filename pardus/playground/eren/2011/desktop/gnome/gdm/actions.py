#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--localstatedir=/var \
                                  --enable-static=no \
                                  --enable-authentication-scheme=shadow \
                                  --disable-scrollkeeper \
                                  --with-pam-prefix=/etc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "TODO")
    # No gnome yet, this package just for xfce, no need to keep gnome desktop file
    pisitools.removeDir("/usr/share/xsessions")

