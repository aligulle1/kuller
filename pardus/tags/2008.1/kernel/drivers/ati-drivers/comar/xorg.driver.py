#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import shutil
import subprocess

import zorg.probe

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
    symlink("xorg/fglrx/lib/libGL.so.1.2", "/usr/lib/libGL.so.1.2")

    # Create other links
    subprocess.call(["/sbin/ldconfig"])

    shutil.copy("/etc/ati/amdpcsdb.default", "/etc/ati/amdpcsdb")

    file("/var/lib/zorg/enabled_package", "w").write("ati-drivers")
    file("/var/lib/zorg/kernel_module", "w").write("fglrx")

    subprocess.call(["/sbin/rmmod", "-s", "fglrx"])
    subprocess.call(["/sbin/modprobe", "-s", "fglrx"])

def disable():
    symlink("xorg/std/lib/libGL.so.1.2", "/usr/lib/libGL.so.1.2")

    unlink("/var/lib/zorg/enabled_package")
    unlink("/var/lib/zorg/kernel_module")

    subprocess.call(["/sbin/rmmod", "-s", "fglrx"])

def probe(device):
    device["depth"] = "24"

    lines = zorg.probe.XProbe(device)
    if not lines:
        return

    tvStandards = [
            "NTSC-M",       "NTSC-JPN", "NTSC-N",      "PAL-B",
            "PAL-COMB-N",   "PAL-D",    "PAL-G",       "PAL-H",
            "PAL-I",        "PAL-K",    "PAL-K1",      "PAL-L",
            "PAL-M",        "PAL-N",    "PAL-SECAM-D", "PAL-SECAM-K",
            "PAL-SECAM-K1", "PAL-SECAM-L"
        ]

    outInfo = re.compile(r".*: Connected Display\d+: (.+) \[(.+)\].*")
    modeCount = re.compile(r".*: Total of \d+ modes found for .* display.*")
    modeLine = re.compile(r".*: Modeline \"(.*)\" *.*")

    primary = ""
    secondary = ""
    outs = []
    parsingModesFor = ""
    outputs = {}

    for line in lines:
        if "Connected Display" in line:
            matched = outInfo.match(line)
            if matched:
                info = matched.groups()
                outs.append(info)
                outputs[info[1]] = []

        elif "Primary Controller - " in line:
            for out in outs:
                if out[0] in line:
                    primary = out[1]

        elif "Secondary Controller - " in line:
            for out in outs:
                if out[0] in line:
                    secondary = out[1]

        elif "modes found for primary display" in line:
            matched = modeCount.match(line)
            if matched:
                parsingModesFor = primary

        elif "modes found for secondary display" in line:
            matched = modeCount.match(line)
            if matched:
                parsingModesFor = secondary

        elif parsingModesFor:
            if "Display dimensions" in line \
                    or "DPI" in line:
                parsingModesFor = ""
                continue

            matched = modeLine.match(line)
            if matched:
                mode = matched.groups()[0]
                if not mode in outputs[parsingModesFor]:
                    outputs[parsingModesFor].append(mode)

    result = {
            "depths":       "24",
            "flags":        "no-modes-line",
            "outputs":      ",".join(outputs.keys()),
            "tv-standards": ",".join(tvStandards)
            }

    for output, modes in outputs.items():
        result["%s-modes" % output] = ",".join(modes)
        if output == primary or modes:
            result["%s-enabled" % output] = "1"
        else:
            result["%s-enabled" % output] = "0"

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
