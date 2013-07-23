#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    enabledPackage = "/var/lib/zorg/enabled_package"
    if os.path.exists(enabledPackage):
        packageName = open(enabledPackage).read()
        if packageName in ("nvidia-drivers-new", "nvidia-drivers173"):
            call("nvidia_drivers173", "Xorg.Driver", "enable")

            if packageName == "nvidia-drivers-new":
                configXML = "/var/lib/zorg/config.xml"
                if os.path.exists(configXML):
                    xmldata = open(configXML).read()
                    xmldata = xmldata.replace("nvidia-drivers-new", "nvidia-drivers173")
                    open(configXML, "w").write(xmldata)
