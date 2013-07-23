#!/usr/bin/python

import os

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    enabledPackage = "/var/lib/zorg/enabled_package"

    if os.path.exists(enabledPackage) and file(enabledPackage).read() == "nvidia-drivers-new":
        call("nvidia_drivers_new", "Xorg.Driver", "enable")

        if fromRelease <= "21":
            symlink("../std/libwfb.so", "/usr/lib/xorg/modules/libwfb.so")
            unlink("/usr/lib/xorg/modules/libnvidia-wfb.so.1")
            unlink("/usr/lib/xorg/modules/libnvidia-wfb.so.173.08")
