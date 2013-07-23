#!/usr/bin/python

import os

def postInstall():
    if not os.path.exists("/usr/share/X11/xkb/compiled"):
        os.symlink("/tmp", "/usr/share/X11/xkb/compiled")

    os.system("/sbin/update-opengl `/sbin/update-opengl --get-implementation`")

