#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

WorkDir="luminance-2.0-SVN691"

def setup():
    shelltools.system("qmake-qt4 PREFIX=/usr \
                       DOCDIR=/usr/share/doc/luminance \
                       HTMLDIR=/usr/share/luminance \
                       I18NDIR=/usr/share/luminance/i18n")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_ROOT=%s"  % get.installDIR())

    for lang in ["cs", "de", "es", "fr", "hu", "id", "it", "pl", "ru", "tr"]:
        shelltools.system("lrelease-qt4 i18n/lang_%(LANG)s.ts -qm i18n/lang_%(LANG)s.qm" % {'LANG':lang} )
    pisitools.insinto("/usr/share/luminance/i18n","i18n/*.qm")

    pisitools.remove("/usr/share/doc/luminance/INSTALL")
