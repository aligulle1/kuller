# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    viewers = { 'PDF' : 'kpdf',
                'PS' : 'kghostview',
                'DVI' : 'kdvi',
                'HTML' : 'konqueror'}

    for k in viewers:
        shelltools.export(k+'_VIEWER', viewers[k])

    autotools.rawConfigure("--prefix=%s/usr" % get.installDIR())

def build():
    autotools.make()

def install():
    autotools.install()

    pythonmodules.fixCompiledPy("/usr/share/lyx/lyx2lyx")
    pythonmodules.fixCompiledPy("/usr/share/lyx/scripts")

    pisitools.dodoc("README*", "ChangeLog", "NEWS", "COPYING", "ANNOUNCE")
