#!/usr/bin/python

import os
import subprocess

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    libGL = "/usr/lib/libGL.so.1.2"
    if not os.path.exists(libGL):
        # Headers
        includedir = "/usr/lib/xorg/std/include"
        for header in os.listdir(includedir):
            symlink(os.path.join(includedir, header), os.path.join("/usr/include/GL", header))

        # Glx library
        symlink("../../std/extensions/libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")
        symlink("xorg/std/lib/libGL.la", "/usr/lib/libGL.la")
        symlink("xorg/std/lib/libGL.so.1.2", libGL)

        symlink("../std/libwfb.so", "/usr/lib/xorg/modules/libwfb.so")

        # Create other links
        subprocess.call(["/sbin/ldconfig"])
