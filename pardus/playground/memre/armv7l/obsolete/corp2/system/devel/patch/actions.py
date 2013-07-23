#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cache = [ "ac_cv_func_strnlen_working=yes",
              "ac_cv_have_decl_strnlen=yes",
              "ac_cv_path_ed_PROGRAM=ed" ]

    crosstools.configure(cache=cache)

def build():
    crosstools.make('LDFLAGS="%(LDFLAGS)s"' % crosstools.environment)

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README")
