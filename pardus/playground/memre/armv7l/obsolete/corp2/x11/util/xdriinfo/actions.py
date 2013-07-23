#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008,2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools

def setup():
    cache = [ "ac_cv_search_glXGetProcAddressARB=-lGL", ]
    autotools.configure(cache=cache)

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
