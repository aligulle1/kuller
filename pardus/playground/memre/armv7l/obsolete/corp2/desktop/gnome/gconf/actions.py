#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="GConf-%s" % get.srcVERSION()

def setup():
    import os
    orbitidl2 = os.popen("which orbit-idl-2").readline().strip()

    pisitools.dosed("gconf/Makefile.in", r'(^ORBIT_IDL\s*=).*', '\\1 %s' % orbitidl2)
    autotools.configure("--disable-static \
                         --without-openldap \
                         --enable-gtk \
                         POLKIT_POLICY_FILE_VALIDATE=true")

    pisitools.dosed("libtool"," -shared "," -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("README", "TODO", "NEWS", "ChangeLog", "AUTHORS")
