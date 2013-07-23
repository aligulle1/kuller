#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="dbp-%s" % get.srcVERSION()

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/gimp/2.0/plug-ins", "dbp")
