#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "Markdown-%s" % get.srcVERSION()

extensions = "%s/%s/extensions" % (get.docDIR(), get.srcNAME())

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()

    pisitools.rename("usr/bin/markdown.py","markdown")

    for i in ['docs/AUTHORS', 'docs/CHANGE_LOG', 'docs/README*', 'docs/*.txt']:
        pisitools.dodoc(i)

    shelltools.chmod("docs/extensions/*", 0644)
    pisitools.insinto(extensions, "docs/extensions/*")
