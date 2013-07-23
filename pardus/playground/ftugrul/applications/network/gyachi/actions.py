#!/usr/bin/python
# -*- coding: utf-8 -*-

#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

def setup():
    os.system("./autogen.sh")
    shelltools.export("CPPFLAGS", "-I/usr/include/gpgme")
#    autotools.configure("--disable-rpath --enable-maintainer-mode --enable-v4l2")
    autotools.configure("--disable-rpath \
                         --disable-wine \
                         --disable-gtktest \
                         --disable-glibtest \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")

