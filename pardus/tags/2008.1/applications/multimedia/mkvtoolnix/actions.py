#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir = "%s/%s" % (get.docDIR(), get.srcTAG())

def setup():
    autotools.configure("--enable-gui \
                         --enable-qt \
                         --enable-lzo \
                         --enable-bz2 \
                         --with-flac \
                         --disable-wxwidgets")

def build():
    autotools.make('STRIP="true"')

def install():
    autotools.rawInstall('DESTDIR="%s" STRIP="true"' % get.installDIR())

    for f in ["examples", "doc/mkvmerge-gui.html", "doc/images"]:
        pisitools.insinto(docdir, f)

    pisitools.dodoc("AUTHORS", "ChangeLog", "README", "TODO")
