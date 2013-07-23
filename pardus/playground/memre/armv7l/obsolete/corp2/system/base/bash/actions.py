#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # clfs hacks
    # http://cross-lfs.org/view/clfs-sysroot/arm/final-system/bash.html
    cache = [ "ac_cv_func_mmap_fixed_mapped=yes",
              "ac_cv_func_strcoll_works=yes",
              "ac_cv_func_working_mktime=yes",
              "bash_cv_func_sigsetjmp=present",
              "bash_cv_getcwd_malloc=yes",
              "bash_cv_job_control_missing=present",
              "bash_cv_printf_a_format=yes",
              "bash_cv_sys_named_pipes=present",
              "bash_cv_ulimit_maxfds=yes",
              "bash_cv_under_sys_siglist=yes",
              "bash_cv_unusable_rtsigs=no",
              "gt_cv_int_divbyzero_sigfpe=yes" ]

    crosstools.configure("--without-installed-readline \
                          --disable-profiling \
                          --without-gnu-malloc \
                          --with-curses", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.install()

    pisitools.domove("/usr/bin/bash", "/bin")
    pisitools.dosym("/bin/bash","/bin/sh")
    pisitools.dosym("/bin/bash","/bin/rbash")

    # Compatibility with old skels
    # pisitools.dosym("/etc/bash/bashrc", "/etc/bashrc")

    pisitools.dosym("bash.info", "/usr/share/info/bashref.info")
    pisitools.doman("doc/bash.1", "doc/bashbug.1", "doc/builtins.1", "doc/rbash.1")
    pisitools.dodoc("README", "NEWS", "AUTHORS", "CHANGES", "COMPAT", "Y2K", "doc/FAQ", "doc/INTRO")
