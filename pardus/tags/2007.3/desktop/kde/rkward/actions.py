#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import kde
from pisi.actionsapi import pisitools


def setup():
    kde.configure("--with-r-home=/usr/lib/R \
                   --with-r-includes=/usr/lib/R/include")

def build():
    kde.make()

def install():
    #for installing rbackend mkdir needed directory(for R-2.5.0)
    pisitools.dodir("/usr/lib/R/library")

    kde.install()
    # TODO: this one seems better than the one in kdelibs
    pisitools.remove("%s/share/apps/katepart/syntax/r.xml" % get.kdeDIR())

    # Fix conflict with R
    pisitools.remove("/usr/lib/R/library/R.css")
