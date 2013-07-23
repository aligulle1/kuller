#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="Elixir-%s" % get.srcVERSION()
examples = "%s/%s/examples" % (get.docDIR(), get.srcTAG())

def install():
    pythonmodules.install()
    
    shelltools.chmod("examples/*", 0644)
    pisitools.insinto(examples, "examples/*")

    pisitools.dodoc("AUTHORS", "CHANGES", "LICENSE", "README", "TODO")
