#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="truecrypt-%s-source" % get.srcVERSION()

def build():
    autotools.make("VERBOSE=1 \
                    NOTEST=1 \
                    CC=%s \
                    CXX=%s" % (get.CC(), get.CXX()))

def install():
    pisitools.dobin("Main/truecrypt")

    pisitools.dodoc("*.txt", "Release/Setup Files/*.pdf")
