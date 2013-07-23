#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("test-suite/tests/popen.test", "sleep 999", "sleep 1")

    cache = [ "ac_cv_sys_restartable_syscalls=yes",
              "ac_cv_func_pthread_key_delete=yes",
              "glib_cv_sys_pthread_mutex_trylock_posix=yes",
              "glib_cv_sys_pthread_getspecific_posix=yes",
              "glib_cv_sys_pthread_cond_timedwait_posix=yes",
              "ac_cv_func_pthread_attr_getstack=yes" ]

    autotools.autoreconf("-vif")
    autotools.configure("--disable-error-on-warning \
                         --disable-static \
                         --enable-posix \
                         --enable-networking \
                         --enable-regex \
                         --enable-elisp \
                         --enable-nls \
                         --disable-rpath \
                         --with-threads \
                         --with-modules", cache=cache)

    # Put flags in front of the libs. Needed for --as-needed.
    replace = (r"(\\\$deplibs) (\\\$compiler_flags)", r"\2 \1")
    pisitools.dosed("libtool", *replace)
    pisitools.dosed("*/libtool", *replace)

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
    autotools.install()

    major = ".".join(get.srcVERSION().split(".")[:2])
    pisitools.dodir("/etc/env.d")
    shelltools.echo("%s/etc/env.d/50guile" % get.installDIR(), 'GUILE_LOAD_PATH="/usr/share/guile/%s"' % major)

    pisitools.dodoc("AUTHORS", "ChangeLog", "FAQ", "HACKING", "NEWS", "README", "THANKS")
