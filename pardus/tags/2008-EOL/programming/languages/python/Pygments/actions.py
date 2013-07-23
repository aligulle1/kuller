#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.dohtml("docs/build/*") 
    pisitools.insinto("/usr/share/doc/%s/src/" % get.srcTAG(),"docs/src/*")
    pisitools.doman("docs/pygmentize.1") 

    pisitools.dodoc("AUTHORS", "LICENSE", "CHANGES", "TODO")

