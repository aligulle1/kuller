#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import glob
import subprocess

import zorg.probe

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

def isG80(productId):
    g80_masks = (
            0x0190,
            0x0400,
            0x0420,
            0x05e0,
            0x05f0,
            0x0600,
            0x0610,
            0x0620,
            0x0630,
            0x0640,
            0x06e0,
            0x06f0
            )

    return productId & 0xfff0 in g80_masks

def randrProbe(device):
    lines = zorg.probe.XProbe(device)
    if not lines:
        return

    findOutput = re.compile("^.*: Output (\S+) (.*)$")
    outStates = ("connected", "disconnected", "enabled by config file")

    parsingModesFor = ""
    outputs = {}
    connected = []
    tvStandards = []

    for line in lines:
        if "Output" in line:
            matched = findOutput.match(line)
            if matched:
                name, state = matched.groups()
                if outputs.has_key(name) or not state in outStates:
                    continue
                else:
                    outputs[name] = []
                    if state == "connected":
                        connected.append(name)

        elif "Printing probed modes for output" in line:
            name = line.rsplit(None, 1)[-1]
            if outputs.has_key(name) and not outputs[name]:
                parsingModesFor = name

        elif parsingModesFor:
            fields = line.split()
            if "Modeline" in fields:
                modeWithRate = fields[fields.index("Modeline") + 1]
                mode, rate = modeWithRate.rsplit("x", 1)
                mode = mode.strip('"')

                if not mode in outputs[parsingModesFor]:
                    outputs[parsingModesFor].append(mode)
            else:
                parsingModesFor = ""

        elif "TV standards supported by chip:" in line:
            tvStandards = line.strip().rsplit(": ", 1)[1].split()

    result = {
            "depths":       "24,16",
            "flags":        "randr12,no-modes-line",
            "outputs":      ",".join(outputs.keys()),
            "tv-standards": ",".join(tvStandards)
            }

    for output, modes in outputs.items():
        result["%s-modes" % output] = ",".join(modes)
        if output in connected:
            result["%s-enabled" % output] = "1"
        else:
            result["%s-enabled" % output] = "0"

    return result

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
    randr12_drivers = ["ati", "i810", "intel", "mga", "nouveau", "radeon", "radeonhd"]

    dev = zorg.probe.VideoDevice(busId=device["bus-id"])

    if dev.vendor_id == "10de" and isG80(int(dev.product_id, 16)):
        randr12_drivers.append("nv")

    if device["driver"] in randr12_drivers:
        return randrProbe(device)

def getOptions(device):
    opts = {}

    dsetup = device["desktop-setup"]

    if dsetup != "single" and device["driver"] == "radeonhd":
        opts["RROutputOrder"] = device["active-outputs"]

    return opts
