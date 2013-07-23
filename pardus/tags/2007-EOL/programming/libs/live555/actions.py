#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="live"

def setup():
    shelltools.system("./genMakefiles shared")

def build():
    autotools.make()

def install():
    for directory in ["BasicUsageEnvironment","groupsock","liveMedia","UsageEnvironment"]:
        pisitools.insinto("/usr/include/%s" % directory, "%s/include/*" % directory)
        pisitools.insinto("/usr/lib/", "%s/*.so" % directory)
