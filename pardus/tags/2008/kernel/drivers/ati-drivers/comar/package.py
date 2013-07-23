#!/usr/bin/python

import os
import subprocess

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    enabledPackage = "/var/lib/zorg/enabled_package"

    if os.path.exists(enabledPackage) and file(enabledPackage).read() == "ati-drivers":
        subprocess.call("hav call ati_drivers Xorg.Driver enable")
