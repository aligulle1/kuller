#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


definitions = "CFLAGS= \
               STD_INCLUDE=%s/usr/share/yodl \
               MAN_DIR=%s/usr/share/man \
               DOC_DIR=%s/usr/share/doc/yodl-%s-%s \
               YODL_BIN=%s/usr/bin \
               STD_CONVERSIONS=man" % (get.installDIR(),get.installDIR(),get.installDIR(),get.srcVERSION(),get.srcRELEASE(),get.installDIR())

def setup():
    pisitools.chmod("contrib/build.pl")

def build():
    shelltools.system("%s contrib/build.pl make" % definitions)

def install():
    shelltools.system("%s contrib/build.pl install" % definitions)

