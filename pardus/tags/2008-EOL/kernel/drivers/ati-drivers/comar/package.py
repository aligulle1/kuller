#!/usr/bin/python

import os

from pisi.version import Version

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    enabledPackage = "/var/lib/zorg/enabled_package"

    if os.path.exists(enabledPackage) and file(enabledPackage).read() == "ati-drivers":
        call("ati_drivers", "Xorg.Driver", "enable")

        if fromVersion and Version(fromVersion) < Version("9.3"):
            from zorg import config

            busId = call("zorg", "Xorg.Display", "activeDeviceID")
            device = config.getDeviceInfo(busId)

            if device:
                device.probe_result["flags"] = "randr12"

                config.saveDeviceInfo(device)
                config.saveXorgConfig(device)
