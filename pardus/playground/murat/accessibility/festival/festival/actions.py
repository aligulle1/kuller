#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = "festival"

def setup():
    for file in ["examples/benchmark", "lib/festival.svm", "testsuite/data/modes.scm"]:
        pisitools.dosed(file, "srcTAG", get.srcTAG())

    autotools.configure()

def build():
    autotools.make("REQUIRED_LIBDEPS=''")

def install():
    for bin in ["src/main/festival", "src/main/festival_client", "bin/festival_server_control",
                "bin/text2wave", "lib/etc/unknown_Linux/audsp", "examples/saytime"]:
        pisitools.dobin(bin)

    pisitools.insinto("/usr/lib", "src/lib/*.so*")
    pisitools.insinto("/usr/include/festival", "src/include/*.h")
    pisitools.insinto("/usr/share/festival/lib", "lib/*")
    pisitools.insinto("/usr/share/festival/lib/etc", "lib/etc/email_filter")
    pisitools.insinto("/usr/share/festival/config", "config/*")

    pisitools.domove("/usr/share/festival/lib/festival.el", "/usr/share/emacs/site-lisp")

    pisitools.dodir("/usr/share/festival/voices-multisyn")
    pisitools.dodir("/var/log/festival")
    pisitools.dodir("/var/run/festival")

    pisitools.remove("/usr/share/festival/lib/siteinit.scm")
    pisitools.removeDir("/usr/share/festival/lib/etc")

    pisitools.insinto("/usr/share/doc/%s/examples" % get.srcTAG(), "examples/*")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "LICENSE")

    for root,dirs,files in os.walk(get.installDIR()):
        for name in files:
            if "Makefile" in name:
                shelltools.unlink(os.path.join(root, name))
