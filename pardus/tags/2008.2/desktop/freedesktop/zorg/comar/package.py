# -*- coding: utf-8 -*-

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if "0.90" <= fromVersion <= "0.96":
        from zorg import config

        busId = call("zorg", "Xorg.Display", "activeDeviceID")
        device = config.getDeviceInfo(busId)

        if device:
            config.saveDeviceInfo(device)
            config.saveXorgConfig(device)
