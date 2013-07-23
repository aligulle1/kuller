#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

WorkDir = get.srcNAME()

KeepSpecial = ["libtool"]

def setup():
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static --with-mono --with-vala")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Move bzr plugin to right place
    pisitools.dodir("/usr/lib/%s/site-packages/bzrlib/plugins" % get.curPYTHON())
    pisitools.domove("/usr/share/pyshared/bzrlib/plugins/zeitgeist", "/usr/lib/%s/site-packages/bzrlib/plugins" % get.curPYTHON())
    os.removedirs("%s/usr/share/pyshared/bzrlib/plugins" % get.installDIR())

    #Chromium plugin is not ready yet. For now there is no way to globally install a Chromium plugin
    #Move chromium plugin to right place
    #pisitools.dodir("/usr/lib/chromium-browser/resources")
    #pisitools.domove("/usr/share/opt/google/chrome/resources/zeitgeist_plugin", "/usr/lib/chromium-browser/resources")
    #os.removedirs("%s/usr/share/opt/google/chrome/resources" % get.installDIR())
    pisitools.removeDir("/usr/share/opt/google")
    os.removedirs("%s/usr/share/opt" % get.installDIR())

    #Move vim plugin to right place
    pisitools.dodir("/usr/share/vim/vimfiles/plugin")
    pisitools.domove("/usr/share/vim/vim72/plugin/zeitgeist.vim", "/usr/share/vim/vimfiles/plugin")
    os.removedirs("%s/usr/share/vim/vim72/plugin" % get.installDIR())

    pisitools.removeDir("/usr/share/mozilla")
    pisitools.dodir("/usr/lib/MozillaFirefox/extensions")
    pisitools.domove("/usr/share/xul-ext-zeitgeist", "/usr/lib/MozillaFirefox/extensions", "xpcom_firefox@zeitgeist-project.com")
    pisitools.remove("/usr/lib/MozillaFirefox/extensions/xpcom_firefox@zeitgeist-project.com/components")
    pisitools.domove("/usr/lib/xul-ext-zeitgeist", "/usr/lib/MozillaFirefox/extensions/xpcom_firefox@zeitgeist-project.com", "components")
