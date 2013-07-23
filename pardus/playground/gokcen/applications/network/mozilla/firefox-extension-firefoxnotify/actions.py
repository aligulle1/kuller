#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os
import zipfile

WorkDir = "firefoxnotify-%s" % get.srcVERSION()

extDir = "%s/usr/lib/MozillaFirefox/extensions" % get.installDIR()
#You can learn ID of ext. from install.rdf or by installing extension locally by dragging xpi to firefox
extID = "firefoxnotify@abhishek.mukherjee"
xpi = "FirefoxNotify-nightly.xpi"

def build():
    autotools.make()

def install():
    if not os.path.isdir(extDir):
        shelltools.makedirs(extDir)

    #Right way of installing extensions is firefox -install-global-extension, but it needs X :) so we just unzip to extension/extension_id directory
    #Installing extension by just unzipping has some bad side-effects also, hmm
    fullExtDir = os.path.join(extDir, extID)
    shelltools.makedirs(fullExtDir)
    zipfile.ZipFile(xpi).extractall(fullExtDir)

    pisitools.dodoc("COPYING", "README*")
