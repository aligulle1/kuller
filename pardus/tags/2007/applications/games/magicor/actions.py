#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "magicor-1.0-rc1"
NoStrip = "/"

pythonlib = "/usr/lib/%s/site-packages/" % get.curPYTHON()
sharedir = "/usr/share/magicor"
config = "/etc/magicor.conf"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)
            if name.endswith(".pyc"):
                shelltools.unlink(os.path.join(root, name))

def setup():
    autotools.make("clean")

    for d in ["etc", "magicor", "scripts"]:
        fixperms(d)

    pisitools.dosed("scripts/Magicor.py", "###CONFIG_PATH###", config)
    pisitools.dosed("scripts/Magicor-LevelEditor.py", "###CONFIG_PATH###", config)

    pisitools.dosed("etc/default.conf", "###SHARE_PATH###", sharedir)
    pisitools.dosed("scripts/Magicor-LevelEditor.py", "###GLADE_FILE###", "%s/editor.glade" % sharedir)

def install():
    pisitools.dodir(pythonlib)
    shelltools.copytree("magicor", "%s/%s/" % (get.installDIR(), pythonlib))

    for f in ["Magicor.py", "Magicor-LevelEditor.py"]:
        pisitools.dobin("scripts/%s" % f)

    pisitools.rename("/usr/bin/Magicor.py", "magicor")
    pisitools.rename("/usr/bin/Magicor-LevelEditor.py", "magicor-editor")

    pisitools.dodir(sharedir)
    pisitools.insinto(sharedir, "etc/editor.glade", "magicor-editor.glade")
    pisitools.insinto("/etc", "etc/default.conf", "magicor.conf")

    pisitools.dodoc("COPYRIGHT", "LICENSE", "README")

