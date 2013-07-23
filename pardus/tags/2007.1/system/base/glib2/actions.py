#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "glib-2.12.4"

def setup():
    autotools.configure("--with-threads=posix \
                         --disable-gtk-doc")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Consider invalid UTF-8 filenames as locale-specific.
    # WARN: we should probably move to suggesting G_FILENAME_ENC
    pisitools.dodir("/etc/env.d")
    shelltools.echo("%s/etc/env.d/50glib2" % get.installDIR(),  "G_BROKEN_FILENAMES=1")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "README*", "INSTALL", "NEWS*")
