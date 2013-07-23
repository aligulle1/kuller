#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    autotools.rawInstall("BINDIR=%s/usr/bin DESTDIR=%s/usr/share/sgml/docbook/xsl-stylesheets-%s"
                         % (get.installDIR(),get.installDIR(),get.srcVERSION()))

    pisitools.dodoc("AUTHORS", "BUGS", "COPYING", "NEWS", "README", "RELEASE-NOTES.txt", "TODO")
