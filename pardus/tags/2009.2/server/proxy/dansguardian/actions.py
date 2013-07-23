#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("OPTIMISE","%s" % get.CFLAGS())
    autotools.configure("--with-logdir=/var/log/dansguardian \
                         --with-piddir=/var/run \
                         --enable-pcre \
                         --enable-fancydm \
                         --enable-email \
                         --enable-clamd=yes \
                         --with-proxyuser=clamav \
                         --with-proxygroup=clamav")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/dansguardian/scripts")
    pisitools.dodir("/var/log/dansguardian")
