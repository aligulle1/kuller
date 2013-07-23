#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="htdocs"

def setup():
    pass

def build():
    pass

def install():
    pisitools.dodir("/var/www/localhost/htdocs/care2x")
    shelltools.move("%s/htdocs" % get.workDIR(),"%s/var/www/localhost/htdocs/care2x" % get.installDIR())