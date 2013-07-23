# -*- coding: utf-8 -*-

import os

from zorg.config import *
from zorg.consts import *
from zorg.probe import *
from zorg.utils import *

kernel_module_file = os.path.join(zorgConfigDir, "kernel_module")
pending_file = os.path.join(zorgConfigDir, "pending")

def selectOutput(device):
    outs = device.probe_result["outputs"].split(",")

    if len(outs) == 1:
        device.active_outputs = outs
        return

    for out in outs:
        if device.probe_result.get("%s-enabled" % out, "0") == "1":
            output = out
            break
    else:
        for out in outs:
            modes = device.probe_result.get("%s-modes" % out, "").split(",")
            if modes:
                output = out
                break
        else:
            output = outs[0]

    device.active_outputs = [output]

def ready(boot):
    opts = []
    driver = None

    if boot:
        kernel_opts = getKernelOpt("xorg")
        if kernel_opts:
            opts = kernel_opts

    if os.path.exists(pending_file):
        opts += file(pending_file).read().split(",")
        unlink(pending_file)

    for opt in opts:
        if ":" in opt:
            key, value = opt.split(":", 1)
            if key == "keymap":
                keymap = value.split("/", 1)
                setKeymap(*keymap)

            elif key == "driver":
                driver = value

    if "off" in opts:
        return False
    elif driver or "probe" in opts:
        return initialConfig(driver)
    elif "safe" in opts:
        return safeConfig()

    if not os.path.exists(xorgConf):
        return initialConfig()

    if boot:
        # Check if the active card is changed
        busId = activeDeviceID()
        if busId:
            try:
                device = getDeviceInfo(busId)
            except IOError:
                # Device is not present on specified bus.
                # Check if the new device is configured before.
                newBus = getPrimaryCard()
                if newBus:
                    device = getDeviceInfo(VideoDevice(newBus).getDict()["bus-id"])
                    if device and not device.isChanged():
                        # Yes, it is configured before.
                        # Reenable driver and write xorg.conf.
                        device.enableDriver()
                        saveXorgConfig(device)
                    else:
                        # This is a different card.
                        return initialConfig()
                else:
                    # No card is present.
                    return False
            else:
                if not device or device.isChanged():
                    return initialConfig()

    applyPendingConfig()

    # Check kernel module. Later, this should be done
    # with Xorg.Driver.ready method.
    if os.path.exists(kernel_module_file):
        kernelModule = file(kernel_module_file).read()
        if run("/sbin/modprobe", "-i", kernelModule):
            return safeConfig()

    return True

def initialConfig(preferredDriver=None):
    bus = getPrimaryCard()

    if bus:
        device = VideoDevice(bus)
    else:
        # This machine might be a terminal server with no video cards.
        # We start X and leave the decision to the user.
        return True

    device.query(preferredDriver)
    selectOutput(device)

    saveXorgConfig(device)
    saveDeviceInfo(device)

    return True

def safeConfig():
    bus = getPrimaryCard()

    if bus:
        device = VideoDevice(bus)
    else:
        # See the comment in initialConfig
        return True

    device.probe_result.update({
        "outputs":      "default",
        "tv-standards": ""
    })
    device.monitors["default"] = Monitor()

    saveXorgConfig(device)
    saveDeviceInfo(device)

    return True

def activeDeviceID():
    if not os.path.exists(xorgConf):
        return

    parser = XorgParser()
    parser.parseFile(xorgConf)

    devSec = parser.getSections("Device")[0]
    busId = devSec.get("BusId")

    return busId

#TODO: Remove later
def changeDriver(driver):
    file(pending_file, "w").write("driver:%s" % driver)

def setupScreens(busId, options, firstScreen, secondScreen):
    device = getDeviceInfo(busId)

    if not device:
        return

    dsetup = options.get("desktop-setup", "single")

    if dsetup not in ("single", "clone", "horizontal", "vertical"):
        return

    device.desktop_setup = dsetup

    if options.has_key("depth"):
        device.depth = options["depth"]

    def setMonitor(scr):
        if scr.has_key("monitor-hsync"):
            mon = Monitor()
            mon.vendor  = scr.get("monitor-vendor", mon.vendor)
            mon.model   = scr.get("monitor-model",  mon.model)
            mon.hsync   = scr.get("monitor-hsync",  mon.hsync)
            mon.vref    = scr.get("monitor-vref",   mon.vref )
            device.monitors[scr["output"]] = mon
        else:
            if device.monitors.has_key(scr["output"]):
                del device.monitors[scr["output"]]

    device.active_outputs = [firstScreen["output"]]
    device.modes[firstScreen["output"]] = firstScreen["mode"]
    setMonitor(firstScreen)

    if dsetup != "single":
        device.active_outputs.append(secondScreen["output"])
        device.modes[secondScreen["output"]] = secondScreen["mode"]
        setMonitor(secondScreen)

    device.requestDriverOptions()

    # Remove "no-modes-line" flag. It is used only for initial
    # setup.
    flags = device.probe_result["flags"].split(",")
    if "no-modes-line" in flags:
        flags.remove("no-modes-line")

    device.probe_result["flags"] = ",".join(flags)

    saveXorgConfig(device)
    saveDeviceInfo(device)

def getPendingConfig():
    if not os.path.exists(zorgConfigDir):
        return

    configFile = os.path.join(zorgConfigDir, zorgConfig)

    try:
        doc = piksemel.parse(configFile)
    except OSError:
        return

    pcfg = doc.getTag("PendingConfig")
    if not pcfg:
        return

    config = {"":""}

    driverTag = pcfg.getTag("Driver")
    if driverTag:
        pkg = driverTag.getAttribute("package")
        drv = pcfg.getTagData("Driver")
        config["driver"] = drv + package_sep + pkg

    depth = pcfg.getTagData("Depth")
    if depth:
        config["depth"] = depth

    monitorTag = pcfg.getTag("Monitor")
    if monitorTag:
        config["monitor-vendor"] = monitorTag.getTagData("Vendor") or ""
        config["monitor-model"] = monitorTag.getTagData("Model") or ""
        config["monitor-hsync"] = monitorTag.getTagData("HorizSync")
        config["monitor-vref"] = monitorTag.getTagData("VertRefresh")

    return config

def setPendingConfig(config):
    if not os.path.exists(zorgConfigDir):
        os.mkdir(zorgConfigDir, 0755)

    configFile = os.path.join(zorgConfigDir, zorgConfig)

    try:
        doc = piksemel.parse(configFile)
    except OSError:
        doc = piksemel.newDocument("ZORG")
    else:
        pcfg = doc.getTag("PendingConfig")
        if pcfg:
            pcfg.hide()

    pcfg = doc.insertTag("PendingConfig")

    if config.has_key("driver"):
        if package_sep in config["driver"]:
            drv, pkg = config["driver"].split(package_sep, 1)
        else:
            drv, pkg = config["driver"], "xorg-video"

        driverTag = pcfg.insertTag("Driver")
        driverTag.setAttribute("package", pkg)
        driverTag.insertData(drv)

    if config.has_key("depth"):
        depthTag = pcfg.insertTag("Depth")
        depthTag.insertData(config["depth"])

    if config.has_key("monitor-hsync"):
        tag = pcfg.insertTag("Monitor")
        if config.has_key("monitor-vendor"):
            tag.insertTag("Vendor").insertData(config["monitor-vendor"])
        if config.has_key("monitor-model"):
            tag.insertTag("Model").insertData(config["monitor-model"])

        tag.insertTag("HorizSync").insertData(config["monitor-hsync"])
        if config.has_key("monitor-vref"):
            tag.insertTag("VertRefresh").insertData(config["monitor-vref"])

    f = file(configFile, "w")
    f.write(doc.toPrettyString().replace("\n\n", ""))
    f.close()

def removePendingConfig():
    if not os.path.exists(zorgConfigDir):
        return

    configFile = os.path.join(zorgConfigDir, zorgConfig)
    doc = piksemel.parse(configFile)

    pcfg = doc.getTag("PendingConfig")
    if pcfg:
        pcfg.hide()

    f = file(configFile, "w")
    f.write(doc.toPrettyString().replace("\n\n", ""))
    f.close()

def applyPendingConfig():
    config = getPendingConfig()
    if not config:
        return

    bus = getPrimaryCard()

    if bus:
        device = VideoDevice(bus)
    else:
        return

    device.query(config.get("driver"))
    selectOutput(device)

    if config.has_key("depth"):
        device.depth = config["depth"]

    if config.has_key("monitor-hsync"):
        out = device.active_outputs[0]
        mon = Monitor()
        mon.vendor = config["monitor-vendor"]
        mon.model  = config["monitor-model"]
        mon.hsync  = config["monitor-hsync"]
        mon.vref   = config["monitor-vref"]
        device.monitors[out] = mon

    saveXorgConfig(device)
    saveDeviceInfo(device)
    removePendingConfig()

def setKeymap(layout, variant="basic"):
    import piksemel

    # FDI file for evdev driver
    doc = piksemel.newDocument("deviceinfo")
    device = doc.insertTag("device")

    match = device.insertTag("match")
    match.setAttribute("key", "info.capabilities")
    match.setAttribute("contains", "input.keys")

    merge = match.insertTag("merge")
    merge.setAttribute("key", "input.xkb.layout")
    merge.setAttribute("type", "string")
    merge.insertData(layout)

    merge = match.insertTag("merge")
    merge.setAttribute("key", "input.xkb.variant")
    merge.setAttribute("type", "string")
    if variant:
        merge.insertData(variant)

    file("/etc/hal/fdi/policy/10-keymap.fdi", "w").write(doc.toPrettyString())

    # zorg's config file
    saveKeymap(layout, variant)

    # xorg.conf
    if os.path.exists(xorgConf):
        parser = XorgParser()
        parser.parseFile(xorgConf)

        inputs = parser.getSections("InputDevice")

        for input in inputs:
            if input.get("Driver") == "kbd":
                input.options["XkbLayout"] = layout
                input.options["XkbVariant"] = variant

        file(xorgConf, "w").write(parser.toString())
