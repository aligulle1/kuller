#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob
import subprocess

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

#
# Çomar methods
#

def enable():
    for oldlib in glob.glob("/usr/lib/libGL.so.*"):
        unlink(oldlib)

    # Glx library
    symlink("../../std/extensions/libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")
    symlink("../../std/extensions/libdri.so", "/usr/lib/xorg/modules/extensions/libdri.so")
    symlink("xorg/std/lib/libGL.la", "/usr/lib/libGL.la")
    symlink("xorg/std/lib/libGL.so.1.2", "/usr/lib/libGL.so.1.2")

    symlink("../std/libwfb.so", "/usr/lib/xorg/modules/libwfb.so")

    # Create other links
    subprocess.call(["/sbin/ldconfig"])

    unlink("/var/lib/zorg/enabled_package")

def disable():
    pass

def probe(device):
    result = {
            "depths":       "24,16",
            "flags":        "randr12,no-modes-line",
            "outputs":      "VBOX1",
            "tv-standards": ""
            }

    return result

def getOptions(device):
    return {}
