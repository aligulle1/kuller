#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown root:ecryptfs /sbin/mount.ecryptfs_private")
    os.chmod("/sbin/mount.ecryptfs_private", 04750)
