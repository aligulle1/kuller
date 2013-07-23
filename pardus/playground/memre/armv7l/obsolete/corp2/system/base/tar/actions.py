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
    cache = [ "gl_cv_func_wcwidth_works=yes",
              "gl_cv_func_btowc_eof=yes",
              "ac_cv_func_malloc_0_nonnull=yes",
              "ac_cv_func_realloc_0_nonnull=yes",
              "gl_cv_func_mbrtowc_incomplete_state=yes",
              "gl_cv_func_mbrtowc_nul_retval=yes",
              "gl_cv_func_mbrtowc_null_arg=yes",
              "gl_cv_func_mbrtowc_retval=yes",
              "gl_cv_func_wcrtomb_retval=yes" ]

    crosstools.configure("--enable-backup-scripts \
                          --bindir=/bin \
                          --libexecdir=/usr/sbin \
                          --enable-nls", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.rename("/usr/sbin/backup","backup-tar")
    pisitools.rename("/usr/sbin/restore","restore-tar")

    pisitools.dosym("/usr/sbin/rmt", "/etc/rmt")

    pisitools.doman("doc/tar.1")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS")
