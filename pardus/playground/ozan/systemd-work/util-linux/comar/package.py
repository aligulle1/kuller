#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.islink("/etc/mtab"):
        os.symlink("/proc/mounts", "/etc/mtab")

    if os.path.exists("/etc/blkid.tab"):
        os.rename("/etc/blkid.tab", "/etc/blkid/blkid.tab")

    if os.path.exists("/etc/blkid.tab.old"):
        os.rename("/etc/blkid.tab.old", "/etc/blkid/blkid.tab.old")

