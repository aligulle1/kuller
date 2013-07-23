#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ORBit2-%s" % get.srcVERSION()

def setup():
    cache = [ "ac_cv_alignof_CORBA_boolean=1",
              "ac_cv_alignof_CORBA_char=1",
              "ac_cv_alignof_CORBA_double=8",
              "ac_cv_alignof_CORBA_float=4",
              "ac_cv_alignof_CORBA_long=4",
              "ac_cv_alignof_CORBA_long_double=8",
              "ac_cv_alignof_CORBA_long_long=8",
              "ac_cv_alignof_CORBA_octet=1",
              "ac_cv_alignof_CORBA_pointer=4",
              "ac_cv_alignof_CORBA_short=2",
              "ac_cv_alignof_CORBA_struct=1",
              "ac_cv_alignof_CORBA_wchar=2",
              "ac_cv_func_getaddrinfo=yes" ]

    autotools.configure("--disable-static \
                         --with-idl-compiler=`which orbit-idl-2`", cache=cache)
    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "TODO")
