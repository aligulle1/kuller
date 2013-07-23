#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import qt4

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

    for lang in ["cs", "de", "es", "fr", "hu", "id", "it", "pl", "ru", "tr"]:
        shelltools.system("lrelease i18n/lang_%(LANG)s.ts -qm i18n/lang_%(LANG)s.qm" % {'LANG':lang} )
    pisitools.insinto("/usr/share/qtpfsgui/i18n","i18n/*.qm")

    pisitools.dodoc("AUTHORS","Changelog", "LICENSE", "README", "TODO")
