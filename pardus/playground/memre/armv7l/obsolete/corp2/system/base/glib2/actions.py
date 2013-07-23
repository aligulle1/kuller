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

WorkDir = "glib-%s" % get.srcVERSION()

def setup():
    shelltools.export("LC_ALL", "C")

    cache = [ "glib_cv_sizeof_gmutex=${glib_cv_sizeof_gmutex=24}",
              "glib_cv_sizeof_system_thread=${glib_cv_sizeof_system_thread=4}",
              "glib_cv_stack_grows=${glib_cv_stack_grows=no}",
              "glib_cv_uscore=${glib_cv_uscore=no}",
              "glib_cv_use_pid_surrogate=${glib_cv_use_pid_surrogate=yes}",
              "glib_cv_has__inline=${glib_cv_has__inline=yes}",
              "glib_cv_has__inline__=${glib_cv_has__inline__=yes}",
              "glib_cv_hasinline=${glib_cv_hasinline=yes}",
              "glib_cv_sane_realloc=${glib_cv_sane_realloc=yes}",
              "glib_cv_sizeof_gmutex=${glib_cv_sizeof_gmutex=24}",
              "glib_cv_uscore=${glib_cv_uscore=no}",
              "glib_cv_va_copy=${glib_cv_va_copy=yes}",
              "glib_cv_va_val_copy=${glib_cv_va_val_copy=yes}",
              "glib_cv___va_copy=${glib_cv___va_copy=yes}",
              "glib_cv_rtldglobal_broken=${glib_cv_rtldglobal_broken=no}",
              "glib_cv_sys_pthread_mutex_trylock_posix=${glib_cv_sys_pthread_mutex_trylock_posix=yes}",
              "glib_cv_sys_pthread_getspecific_posix=${glib_cv_sys_pthread_getspecific_posix=yes}",
              "glib_cv_sys_pthread_cond_timedwait_posix=${glib_cv_sys_pthread_cond_timedwait_posix=yes}",
              "glib_cv_long_long_format=${glib_cv_long_long_format=ll}",
              "glib_cv_sizeof_gmutex=${glib_cv_sizeof_gmutex=24}",
              "glib_cv_sizeof_intmax_t=${glib_cv_sizeof_intmax_t=8}",
              "glib_cv_sizeof_ptrdiff_t=${glib_cv_sizeof_ptrdiff_t=4}",
              "glib_cv_sizeof_size_t=${glib_cv_sizeof_size_t=4}",
              "glib_cv_sizeof_system_thread=${glib_cv_sizeof_system_thread=4}",
              "glib_cv_sys_use_pid_niceness_surrogate=${glib_cv_sys_use_pid_niceness_surrogate=yes}",
              "ac_cv_c_littleendian=${ac_cv_c_littleendian=yes}",
              "ac_cv_c_bigendian=${ac_cv_c_bigendian=no}",
              "ac_cv_libnet_endianess=${ac_cv_libnet_endianess=lil}"
              "ac_cv_func_lstat_dereferences_slashed_symlink=${ac_cv_func_lstat_dereferences_slashed_symlink=yes}",
              "ac_cv_func_lstat_empty_string_bug=${ac_cv_func_lstat_empty_string_bug=no}",
              "ac_cv_func_stat_empty_string_bug=${ac_cv_func_stat_empty_string_bug=no}",
              "ac_cv_func_stat_ignores_trailing_slash=${ac_cv_func_stat_ignores_trailing_slash=no}",
              "ac_cv_header_netinet_sctp_h=${ac_cv_header_netinet_sctp_h=no}",
              "ac_cv_header_netinet_sctp_uio_h=${ac_cv_header_netinet_sctp_uio_h=no}",
              "ac_cv_sctp=${ac_cv_sctp=no}",
              "ac_cv_header_pwd_h=${ac_cv_header_pwd=yes}",
              "ac_cv_func_posix_getpwuid_r=${ac_cv_func_posix_getpwuid_r=yes}",
              "ac_cv_func_posix_getgrgid_r=${ac_cv_func_posix_getgrgid_r=yes}" ]

    crosstools.autoconf()
    crosstools.configure("--with-threads=posix \
                          --disable-gtk-doc \
                          --with-pcre=system \
                          --disable-fam \
                          --disable-static", cache=cache)

    pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.removeDir("/usr/share/gtk-doc")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "README*", "NEWS*")
