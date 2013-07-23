#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi.libtools import gnuconfig_update
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

import os

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(os.path.join(root, name), 0644)

def setup():
    gnuconfig_update()

    autotools.configure("--enable-opengl \
                         --disable-editors \
                         --disable-sdltest \
                         --disable-gtktest \
                         --with-x \
                         --with-sdl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Croppy is a standalone program to post-process png files. It crops PNG files to teh smallest dimension without losing data. So, we don't need this for game play...
    pisitools.remove("/usr/bin/croppy")

    # Pngtoico takes the FDRPG png files and turns them into Win32 .ico files and then those .ico files get compiled into the Win32 binary. So, we don't need this neither for game play...
    pisitools.remove("/usr/bin/pngtoico")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FILES", "HELP_WANTED", "INSTALL*", "IDEAS", "NEWS", "README")

    for d in ["dialogs", "graphics", "map", "sound"]:
        fixperms("%s/usr/share/freedroidrpg/%s" % (get.installDIR(), d))
