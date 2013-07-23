#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import subprocess

version = "180.22"
major = version.split(".")[0]
base = "/usr/lib/xorg/nvidia-%s" % major

def unlink(name):
    if os.path.lexists(name):
        os.unlink(name)

def symlink(src, dst):
    unlink(dst)
    os.symlink(src, dst)

links = (
        # X driver
        ("%s/drivers/nvidia_drv.so" % base, "/usr/lib/xorg/modules/drivers/nvidia_drv.so"),

        # XvMC library
        ("%s/lib/libXvMCNVIDIA.so.%s" % (base, version), "/usr/lib/libXvMCNVIDIA.so.%s" % version),
        ("libXvMCNVIDIA.so.%s" % version, "/usr/lib/libXvMCNVIDIA.so"),

        # glx extension
        ("%s/extensions/libglx.so.%s" % (base, version), "/usr/lib/xorg/modules/extensions/libglx.so"),

        # GL library
        ("%s/lib/libGL.la" % base, "/usr/lib/libGL.la"),
        ("%s/lib/libGL.so.%s" % (base, version), "/usr/lib/libGL.so.1.2"),

        ("libGLcore.so.1", "/usr/lib/libGLcore.so"),
        ("libGLcore.so.%s" % version, "/usr/lib/libGLcore.so.1"),
        ("%s/lib/libGLcore.so.%s" % (base, version), "/usr/lib/libGLcore.so.%s" % version),

        # Cuda library
        ("libcuda.so.1", "/usr/lib/libcuda.so"),
        ("libcuda.so.%s" % version, "/usr/lib/libcuda.so.1"),
        ("%s/lib/libcuda.so.%s" % (base, version), "/usr/lib/libcuda.so.%s" % version),
        ("%s/include/cuda" % base, "/usr/include/cuda"),

        # VDPAU libraries
        ("libvdpau.so.1", "/usr/lib/libvdpau.so"),
        ("libvdpau.so.%s" % version, "/usr/lib/libvdpau.so.1"),
        ("%s/lib/libvdpau.so.%s" % (base, version), "/usr/lib/libvdpau.so.%s" % version),

        ("libvdpau_trace.so.%s" % version, "/usr/lib/libvdpau_trace.so"),
        ("%s/lib/libvdpau_trace.so.%s" % (base, version), "/usr/lib/libvdpau_trace.so.%s" % version),

        ("libvdpau_nvidia.so.%s" % version, "/usr/lib/libvdpau_nvidia.so"),
        ("%s/lib/libvdpau_nvidia.so.%s" % (base, version), "/usr/lib/libvdpau_nvidia.so.%s" % version),

        ("%s/include/vdpau" % base, "/usr/include/vdpau"),

        # nvidia-cfg library
        ("libnvidia-cfg.so.1", "/usr/lib/libnvidia-cfg.so"),
        ("libnvidia-cfg.so.%s" % version, "/usr/lib/libnvidia-cfg.so.1"),
        ("%s/lib/libnvidia-cfg.so.%s" % (base, version), "/usr/lib/libnvidia-cfg.so.%s" % version),

        # nvidia-tls library
        ("libnvidia-tls.so.1", "/usr/lib/libnvidia-tls.so"),
        ("libnvidia-tls.so.%s" % version, "/usr/lib/libnvidia-tls.so.1"),
        ("%s/lib/tls/libnvidia-tls.so.%s" % (base, version), "/usr/lib/libnvidia-tls.so.%s" % version),
        )

#
# Çomar methods
#

def enable():
    for src, dst in links:
        symlink(src, dst)

    # Create other links
    subprocess.call(["/sbin/ldconfig"])

    file("/var/lib/zorg/enabled_package", "w").write("nvidia-drivers%s" % major)
    file("/var/lib/zorg/kernel_module", "w").write("nvidia_%s" % major)

    subprocess.call(["/sbin/rmmod", "-s", "nvidia"])
    subprocess.call(["/sbin/modprobe", "-s", "nvidia"])

def disable():
    for src, dst in links:
        unlink(dst)

    symlink("../../std/extensions/libglx.so", "/usr/lib/xorg/modules/extensions/libglx.so")
    symlink("xorg/std/lib/libGL.la", "/usr/lib/libGL.la")
    symlink("xorg/std/lib/libGL.so.1.2", "/usr/lib/libGL.so.1.2")

    unlink("/var/lib/zorg/enabled_package")
    unlink("/var/lib/zorg/kernel_module")

    subprocess.call(["/sbin/rmmod", "-s", "nvidia"])

def probe(device):
    import zorg.probe

    lines = zorg.probe.XProbe(device)
    if not lines:
        return

    tvStandards = [
            "PAL-B",  "PAL-D",  "PAL-G",   "PAL-H",
            "PAL-I",  "PAL-K1", "PAL-M",   "PAL-N",
            "PAL-NC", "NTSC-J", "NTSC-M",  "HD480i",
            "HD480p", "HD720p", "HD1080i", "HD1080p",
            "HD576i", "HD576p"
        ]

    parsingModesFor = ""
    outputs = {}
    assigned = ""

    for line in lines:
        if "Supported display device(s): " in line:
            outs = line.rsplit(":", 1)[-1].split(",")
            for out in outs:
                out = out.strip()
                outputs[out] = []

        elif "--- Modes in ModePool for " in line:
            for key in outputs.keys():
                if key in line:
                    parsingModesFor = key
                    break

        elif parsingModesFor:
            if "--- End of ModePool for " in line:
                parsingModesFor = ""
                continue

            mode = line.split(":")[2].split("@", 1)[0].replace(" ", "")

            if not mode in outputs[parsingModesFor]:
                outputs[parsingModesFor].append(mode)

        elif "Assigned Display Device: " in line:
            assigned = line.rsplit(":", 1)[-1].strip()

    result = {
            "depths":       "24,16",
            "flags":        "",
            "outputs":      ",".join(outputs.keys()),
            "TVStandards":  ",".join(tvStandards)
            }

    for output, modes in outputs.items():
        result["%s-modes" % output] = ",".join(modes)
        if output == assigned:
            result["%s-enabled" % output] = "1"
        else:
            result["%s-enabled" % output] = "0"

    return result

def getOptions(device):
    opts = {}

    dsetup = device["desktop-setup"]
    active_outputs = device["active-outputs"].split(",")

    out1 = active_outputs[0]
    mode1 = device.get("%s-mode" % out1, "nvidia-auto-select")

    hsync = ""
    vref = ""

    if device.has_key("%s-hsync" % out1):
        hsync = "%s: %s" % (out1, device["%s-hsync" % out1])

    if device.has_key("%s-vref" % out1):
        vref = "%s: %s" % (out1, device["%s-vref" % out1])

    if dsetup == "single":
        opts["MetaModes"] = "%s: %s" % (out1, mode1)

    else:
        opts["TwinView"] = "True"
        opts["TwinViewXineramaInfoOrder"] = device["active-outputs"]

        out2 = active_outputs[1]
        mode2 = device.get("%s-mode" % out2, "nvidia-auto-select")
        modes = (out1, mode1, out2, mode2)

        if dsetup == "clone":
            opts["MetaModes"] = "%s: %s +0+0, %s: %s +0+0" % modes
            opts["TwinViewOrientation"] = "%s Clone %s" % (out1, out2)

        elif dsetup == "horizontal":
            opts["MetaModes"] = "%s: %s, %s: %s" % modes
            opts["TwinViewOrientation"] = "%s LeftOf %s" % (out1, out2)

        elif dsetup == "vertical":
            opts["MetaModes"] = "%s: %s, %s: %s" % modes
            opts["TwinViewOrientation"] = "%s Above %s" % (out1, out2)

        if device.has_key("%s-hsync" % out2):
            if hsync:
                hsync += "; "
            hsync += "%s: %s" % (out2, device["%s-hsync" % out2])

        if device.has_key("%s-vref" % out2):
            if vref:
                vref += "; "
            vref += "%s: %s" % (out2, device["%s-vref" % out2])

    if hsync:
        opts["HorizSync"] = hsync

    if vref:
        opts["VertRefresh"] = vref

    return opts
