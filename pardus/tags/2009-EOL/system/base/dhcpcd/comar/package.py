#!/usr/bin/python
import os
import glob
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if fromVersion.startswith("3"):
        # Migrate from old dhcpcd
        old_duid = "/var/lib/dhcpcd/dhcpcd.duid"
        new_duid = "/etc/dhcpcd.duid"

        if os.path.exists(old_duid):
            shutil.copy(old_duid, new_duid)

def preRemove():
    pass
