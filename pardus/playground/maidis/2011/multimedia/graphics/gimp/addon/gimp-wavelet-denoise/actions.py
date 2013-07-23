#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.dolib("src/wavelet-denoise", "/usr/lib/gimp/2.0/plug-ins")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "THANKS", "TRANSLATIONS")

    shelltools.cd("po")

    autotools.rawInstall("LOCALEDIR=%s/usr/share/locale DESTDIR=%s" % (get.installDIR(), get.installDIR()))
