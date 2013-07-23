#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "alsa-driver-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/include/sound/", "alsa-kernel/include/*.h")
