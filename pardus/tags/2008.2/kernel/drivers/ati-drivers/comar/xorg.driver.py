#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import shutil
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
    symlink("/usr/lib/xorg/fglrx/lib/libGL.so.1.2",     "/usr/lib/libGL.so.1.2")
    symlink("/usr/lib/xorg/fglrx/extensions/libdri.so", "/usr/lib/xorg/modules/extensions/libdri.so")

    # Create other links
    subprocess.call(["/sbin/ldconfig"])

    shutil.copy("/etc/ati/amdpcsdb.default", "/etc/ati/amdpcsdb")

    file("/var/lib/zorg/enabled_package", "w").write("ati-drivers")
    file("/var/lib/zorg/kernel_module", "w").write("fglrx")

    subprocess.call(["/sbin/rmmod", "-s", "fglrx", "radeon"])
    subprocess.call(["/sbin/modprobe", "-s", "fglrx"])

def disable():
    symlink("/usr/lib/xorg/std/lib/libGL.so.1.2",       "/usr/lib/libGL.so.1.2")
    symlink("/usr/lib/xorg/std/extensions/libdri.so",   "/usr/lib/xorg/modules/extensions/libdri.so")

    unlink("/var/lib/zorg/enabled_package")
    unlink("/var/lib/zorg/kernel_module")

    subprocess.call(["/sbin/rmmod", "-s", "fglrx"])

def probe(device):
    device["depth"] = "24"

    tvStandards = [
            "NTSC-M",       "NTSC-JPN", "NTSC-N",      "PAL-B",
            "PAL-COMB-N",   "PAL-D",    "PAL-G",       "PAL-H",
            "PAL-I",        "PAL-K",    "PAL-K1",      "PAL-L",
            "PAL-M",        "PAL-N",    "PAL-SECAM-D", "PAL-SECAM-K",
            "PAL-SECAM-K1", "PAL-SECAM-L"
        ]

    result = {
            "depths":       "24",
            "flags":        "no-modes-line",
            "outputs":      "auto",
            "auto-enabled": "1",
            "tv-standards": ",".join(tvStandards)
            }

    return result

def getOptions(device):
    opts = {}

    dsetup = device["desktop-setup"]
    opts["EnableMonitor"] = device["active-outputs"]

    if dsetup == "single":
        return opts

    active_outputs = device["active-outputs"].split(",")

    opts["DesktopSetup"] = dsetup

    out2 = active_outputs[1]

    if device.has_key("%s-mode" % out2):
        opts["Mode2"] = device["%s-mode" % out2]

    if device.has_key("%s-hsync" % out2):
        opts["HSync2"] = device["%s-hsync" % out2]

    if device.has_key("%s-vref" % out2):
        opts["VRefresh2"] = device["%s-vref" % out2]

    return opts
