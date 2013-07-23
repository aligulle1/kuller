#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    # don't log so much...
    pisitools.dosed("Util/Logger.cs", "defaultLevel = LogLevel.Debug", "defaultLevel = LogLevel.Info/")

    shelltools.export("WANT_AUTOCONF", "2.5")

    autotools.autoreconf("-f -i")
    autotools.automake()

    autotools.configure("--enable-python --enable-libbeagle --disable-gui")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # FIXME: Firefox Extension
    pisitools.insinto("/usr/share/beagle", "mozilla-extension/beagle.xpi")
    pisitools.dodoc("AUTHORS", "INSTALL", "NEWS", "README")

    # Disable all crawl
    pisitools.dosed("%s/etc/beagle/crawl-*" % get.installDIR(), "CRAWL_ENABLED=\"yes\"", "CRAWL_ENABLED=\"no\"")

    pisitools.dodir("/usr/lib/beagle/Backends")

    # System-wide indexing
    #pisitools.dodir("/var/lib/cache/beagle/indexes")
    #chown -o beagleindex -g beagleindex /var/lib/cache/beagle/indexes
