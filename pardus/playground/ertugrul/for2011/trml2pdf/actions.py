#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import pythonmodules

def install():
    pisitools.insinto("/usr/lib/%s/site-packages/trml2pdf" % get.curPYTHON(),"trml2pdf/*.py")

    pythonmodules.fixCompiledPy()

    # create needed symlink
    pisitools.dosym("/usr/lib/%s/site-packages/trml2pdf/trml2pdf.py" % get.curPYTHON(),"/usr/bin/trml2pdf")

    # add examples and docs
    pisitools.insinto("/usr/share/doc/trml2pdf/examples" , "rmls/*.rml")

    pisitools.dodoc("README.txt","COPYRIGHT.txt")
