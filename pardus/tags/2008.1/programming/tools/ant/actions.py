#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os

WorkDir = "apache-ant-%s" % get.srcVERSION()

def build():
    shelltools.system("./bootstrap.sh")

def install():
    pisitools.cd("src/script")

    for bin in ["antRun", "complete-ant-cmd.pl", "runant.pl", "runant.py"]:
        pisitools.dobin(bin)
        pisitools.dosym("/usr/bin/%s" % bin, "/usr/share/ant-core/bin/%s" % bin)

    pisitools.dobin("ant")

    shelltools.cd("../../bootstrap/lib")
    pisitools.insinto("/usr/share/ant-tasks/lib/", "*.jar")

    for jar in os.listdir("."):
        pisitools.dosym("/usr/share/ant-tasks/lib/%s" % jar, "/usr/share/ant-core/lib/%s" % jar)

    pisitools.dodoc("README", "WHATSNEW", "LICENSE", "docs/*")
