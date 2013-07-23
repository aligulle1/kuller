# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

WorkDir = "lyx-1.5.0beta2"

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
    pisitools.dodoc("README*", "UPGRADING", "ChangeLog", "NEWS", "COPYING", "ANNOUNCE", "ABOUT-NLS" )

    pythonmodules.fixCompiledPy()
