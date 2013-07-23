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
    cache = [ "gl_cv_func_btowc_eof=yes",
              "gl_cv_func_mbrtowc_incomplete_state=yes",
              "gl_cv_func_mbrtowc_sanitycheck=yes",
              "gl_cv_func_mbrtowc_null_arg=yes",
              "gl_cv_func_mbrtowc_retval=yes",
              "gl_cv_func_mbrtowc_nul_retval=yes",
              "gl_cv_func_wcrtomb_retval=yes",
              "gl_cv_func_wctob_works=yes" ]

    crosstools.configure("--enable-nls \
                          --enable-changeword", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("BACKLOG", "ChangeLog", "NEWS", "README*", "THANKS", "TODO")
