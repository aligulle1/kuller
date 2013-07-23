#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

import os

WorkDir = "./"
NoStrip = ["/"]

icondir = "/usr/share/icons"
iconsrc = "milky"

def fixperms(d, workaround=False):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if workaround:
                if name.startswith("system-restart."):
                    shelltools.copy(os.path.join(root, name), os.path.join(root, name.replace("system-restart.", "system-reboot.")))
                if name.startswith("edit-find."):
                    shelltools.copy(os.path.join(root, name), os.path.join(root, name.replace("edit-find.", "../apps/kfind.")))
                if name.startswith("text-plain."):
                    for zetubiyer in ["text-x-authors.", "text-x-changelog.", "text-x-cmake.", "text-x-copying.", "text-x-log.", "text-x-nfo.", "text-x-readme.", "text-x-install."]:
                        shelltools.copy(os.path.join(root, name), os.path.join(root, name.replace("text-plain.", zetubiyer)))


def setup():
    fixperms(iconsrc, workaround=True)

def install():
    pisitools.insinto(icondir, iconsrc)


