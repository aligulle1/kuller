#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("doc/screen.1", "/usr/local/etc/screenrc", "/etc/screenrc")
    pisitools.dosed("doc/screen.1", "/usr/local/screens", "/var/run/screen")
    pisitools.dosed("doc/screen.1", "/local/etc/screenrc", "/etc/screenrc")
    pisitools.dosed("doc/screen.1", "/etc/utmp", "/var/run/utmp")
    pisitools.dosed("doc/screen.1", "/local/screens/S-", "/var/run/screen/S-")

    autotools.environment["CFLAGS"] = "%(CFLAGS)s -DPTYMODE=0620 -DPTYGROUP=5 -DUSE_PAM" % autotools.environment
    autotools.environment["CXXFLAGS"] = "%(CXXFLAGS)s -DPTYMODE=0620 -DPTYGROUP=5 -DUSE_PAM" % autotools.environment

    autotools.autoconf()

    cache = [ "screen_cv_sys_bcopy_overlap=${screen_cv_sys_bcopy_overlap=no}",
              "screen_cv_sys_memcpy_overlap=${screen_cv_sys_memcpy_overlap=no}",
              "screen_cv_sys_memmove_overlap=${screen_cv_sys_memmove_overlap=no}",
              "screen_cv_sys_fifo_broken_impl=${screen_cv_sys_fifo_broken_impl=yes}",
              "screen_cv_sys_fifo_usable=${screen_cv_sys_fifo_usable=yes}",
              "screen_cv_sys_select_broken_retval=${screen_cv_sys_select_broken_retval=no}",
              "screen_cv_sys_sockets_nofs=${screen_cv_sys_sockets_nofs=no}",
              "screen_cv_sys_sockets_usable=${screen_cv_sys_sockets_usable=yes}",
              "screen_cv_sys_terminfo_used=${screen_cv_sys_terminfo_used=yes}" ]

    autotools.configure("--enable-pam \
                         --with-socket-dir=/var/run/screen \
                         --with-sys-screenrc=/etc/screenrc \
                         --enable-rxvt_osc \
                         --enable-colors256 \
                         --with-pty-mode=0620 \
                         --with-pty-group=5", cache=cache)

def build():
    autotools.make("term.h")
    autotools.make()

def install():
    pisitools.dobin("screen")

    pisitools.dodir("/var/run/screen")
    pisitools.dodir("/etc/pam.d")

    pisitools.insinto("/usr/share/terminfo", "terminfo/screencap")
    pisitools.insinto("/usr/share/screen/utf8encodings", "utf8encodings/??")

    shelltools.chmod("%s/var/run/screen" % get.installDIR(), 0775)

    pisitools.doman("doc/screen.1")
    pisitools.doinfo("doc/screen.info*")
    pisitools.dodoc("README", "ChangeLog", "TODO", "NEWS*", "doc/FAQ", "doc/README.DOTSCREEN")
