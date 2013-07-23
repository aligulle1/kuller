#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    shelltools.system("/usr/lib/%s/site-packages/unsermake/unsermake all" % get.curPYTHON())

def install():
    shelltools.system("/usr/lib/%s/site-packages/unsermake/unsermake DESTDIR=%s install" % (get.curPYTHON(), get.installDIR()))
