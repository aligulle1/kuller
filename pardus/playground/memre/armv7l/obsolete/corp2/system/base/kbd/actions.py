#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cache= [ "ac_cv_func_setpgrp_void=yes",
             "ac_cv_func_malloc_0_nonnull=yes",
             "ac_cv_func_realloc_0_nonnull=yes" ]

    crosstools.configure("--enable-nls", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR())

    for exe in ("kbd_mode", \
                "dumpkeys", \
                "openvt", \
                "loadkeys", \
                "setfont", \
                "unicode_start", \
                "unicode_stop"):
        pisitools.domove("/usr/bin/%s" % exe, "/bin")
        pisitools.dosym("../../bin/%s" % exe, "/usr/bin/%s" % exe)

    pisitools.remove("/usr/share/keymaps/i386/qwerty/trf.map.gz")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README")
