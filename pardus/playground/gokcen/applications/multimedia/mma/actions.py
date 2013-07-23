#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="mma-bin-%s" % get.srcVERSION()

def install():
    # mma executable and its utils
    pisitools.insinto("/usr/bin", "mma.py", "mma")
    pisitools.insinto("/usr/bin", "util/mklibdoc.py", "mklibdoc")
    pisitools.insinto("/usr/bin", "util/mma-renum.py", "mma-renum")
    pisitools.insinto("/usr/bin", "util/timsplit.py", "timsplit")
    pisitools.dosed("util/mmatabs.py", "/usr/local/share/mma", "/usr/share/mma")
    pisitools.insinto("/usr/bin", "util/mmatabs.py", "mmatabs")
    pisitools.insinto("/usr/bin", "util/mup2mma.py", "mup2mma")

    # mma libraries, includes, samples and mma module itself
    pisitools.dodir("/usr/share/mma")
    shelltools.copytree("lib", "%s/usr/share/mma/" % get.installDIR())
    shelltools.copytree("includes", "%s/usr/share/mma/" % get.installDIR())
    shelltools.copytree("egs", "%s/usr/share/mma/" % get.installDIR())
    shelltools.copytree("MMA", "%s/usr/share/mma/" % get.installDIR())

    # mma documentation
    pisitools.dodoc("text/*")
    pisitools.dosed("util/README.mklibdoc", "mklibdoc.py", "mklibdoc")
    pisitools.dosed("util/README.mmatabs", "mmatabs.py", "mmatabs")
    pisitools.dosed("util/README.timsplit", "timsplit.py", "timsplit")
    pisitools.dodoc("util/README*")
    shelltools.copytree("docs/html", "%s/usr/share/doc/%s/" % (get.installDIR(), get.srcTAG()))
