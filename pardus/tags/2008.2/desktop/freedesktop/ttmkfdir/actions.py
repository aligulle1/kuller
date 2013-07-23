#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

flags = get.CXXFLAGS().replace("-fstack-protector", "").replace("-O2", "")

def setup():
    #FIXME: find who is to blame...
    shelltools.sym(".", ".libs")

def build():
    autotools.make('CXX="%s" \
                    OPTFLAGS="%s" \
                    DEBUG="" \
                    -j1' % (get.CXX(), flags))

def install():
    pisitools.dobin("ttmkfdir")

    pisitools.dodoc("README")
