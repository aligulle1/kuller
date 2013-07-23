#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("DEFAULT_POSIX2_VERSION", "199209")
    shelltools.export("AUTOPOINT", "/bin/true")
    shelltools.export("AT_M4DIR", "m4")

    # man docs are unneccessary.
    pisitools.dosed("Makefile.in", "(^SUBDIRS\\s*=\\s*).*", "\\1 lib src po tests gnulib-tests")

    # clfs presettings.
    cache = [ "fu_cv_sys_stat_statfs2_bsize=yes",
              "gl_cv_func_rename_trailing_slash_bug=no",
              "gl_cv_func_mbrtowc_incomplete_state=yes",
              "gl_cv_func_mbrtowc_nul_retval=yes",
              "gl_cv_func_mbrtowc_null_arg=yes",
              "gl_cv_func_mbrtowc_retval=yes",
              "gl_cv_func_btowc_eof=yes",
              "gl_cv_func_wcrtomb_retval=yes",
              "gl_cv_func_wctob_works=yes",
              "gl_cv_func_working_mkstemp=yes",
              "gl_cv_func_printf_directive_n=yes",
              "gl_cv_func_isnanl_works=yes",
              "gl_cv_func_working_acl_get_file=yes" ]

    crosstools.configure("--enable-largefile \
                          --enable-nls \
                          --enable-acl \
                          --enable-xattr \
                          --enable-install-program=arch \
                          --disable-libcap \
                          --without-included-regex \
                          --without-gmp \
                          --enable-no-install-program=faillog,hostname,login,lastlog,uptime", cache=cache)

def build():
    crosstools.make('LDFLAGS="%(LDFLAGS)s"' % crosstools.environment)

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Use dircolors from the package
    pisitools.insinto("/etc", "src/dircolors.hin", "DIR_COLORS")

    # move critical files into /bin
    for file in ["cat","chgrp","chmod","chown","cp","date","dd","df",
                 "dir","echo","false","ln","ls","mkdir","mknod","mv",
                 "pwd","readlink","rm","rmdir","sleep","stty","sync",
                 "touch","true","uname","vdir"]:
        pisitools.domove("/usr/bin/%s" % file, "/bin/")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS", "TODO")
