#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-nls \
                         --disable-java \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Hack for http://www.opensubscriber.com/message/help-libidn@gnu.org/6965899.html
    pisitools.remove("/usr/include/idn-int.h")
    pisitools.echo("%s/usr/include/idn-int.h" % get.installDIR(),"#include <stdint.h>")

    pisitools.dohtml("doc/reference/html/")
    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ", "NEWS", "README", "THANKS", "TODO")
