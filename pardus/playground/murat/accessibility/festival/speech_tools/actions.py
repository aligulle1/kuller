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

WorkDir = "speech_tools"

def setup():
    shelltools.export("CC_OTHER_FLAGS", get.CFLAGS())

    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/speech_tools/example_data", "lib/example_data/*")

    for files in os.listdir("bin"):
        pisitools.doexe("main/%s" % files, "/usr/lib/speech_tools/main")
        pisitools.dosed("bin/%s" % files, "%s/%s/lib" % (get.workDIR(), WorkDir), "/usr/lib")
        pisitools.dosed("bin/%s" % files, "%s/%s/main" % (get.workDIR(), WorkDir), "/usr/lib/speech_tools/main")
        pisitools.dobin("bin/%s" % files)

    pisitools.insinto("/usr/lib", "lib/*.so*")
    pisitools.insinto("/usr/lib/speech_tools/scripts", "scripts/*")
    pisitools.insinto("/usr/lib/speech_tools/config", "config/*")
    pisitools.insinto("/usr/lib/speech_tools/testsuite", "testsuite/*")
    pisitools.insinto("/usr/lib/speech_tools/siod", "siod/siod.mak")
    pisitools.insinto("/usr/lib/speech_tools/siod", "lib/siod/*.scm")
    pisitools.insinto("/usr/lib/speech_tools/stats", "stats/old.mak")
    pisitools.insinto("/usr/lib/speech_tools/stats/wagon", "stats/wagon/wagon.mak")
    pisitools.insinto("/usr/lib/speech_tools/grammar/scfg", "grammar/scfg/scfg.mak")
    pisitools.insinto("/usr/lib/speech_tools/grammar/wfst", "grammar/wfst/wfst.mak")

    pisitools.insinto("/usr/include/EST", "include/*")

    for root,dirs,files in os.walk("%s/usr/include/EST" % get.installDIR()):
        for header in files:
            pisitools.dosed(os.path.join(root, header) , '#include "(.*h)\"','#include <EST/\\1>')

    pisitools.dosed("%s/usr/include/EST/rxp/rxp.h" % get.installDIR(), "EST/", "EST/rxp/")

    for root,dirs,files in os.walk(get.installDIR()):
        for name in files:
            if name.endswith(".cc") or name.endswith(".o") or "Makefile" in name:
                shelltools.unlink(os.path.join(root, name))

    for files in os.listdir("%s/usr/include/EST/rxp" % get.installDIR()):
        pisitools.dosym("/usr/include/EST/rxp/%s" % files, "/usr/include/EST/%s" % files)

    pisitools.removeDir("/usr/include/EST/win32")

    pisitools.dodoc("README")
