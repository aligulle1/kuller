#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # Disable SSE on x86, but leave it intact for x86_64
    sse_conf = "" if get.ARCH() == "x86_64" else "--disable-sse"

    autotools.configure("--disable-static \
                         --with-pic %s" % sse_conf)

    pisitools.dosed('libtool', '^hardcode_libdir_flag_spec=.*', 'hardcode_libdir_flag_spec=""')
    pisitools.dosed('libtool', '^runpath_var=LD_RUN_PATH', 'runpath_var=DIE_RPATH_DIE')

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING", "HACKING", "README", "NEWS")
