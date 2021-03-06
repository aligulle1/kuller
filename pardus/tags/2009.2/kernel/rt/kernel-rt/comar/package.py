#!/usr/bin/python

import os.path
import subprocess

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    KVER = open("/etc/kernel/kernel-rt").read().strip()

    # Create initramfs image
    subprocess.call(["/sbin/mkinitramfs", "--type", "kernel-rt"])

    # Update GRUB entry
    if os.path.exists("/boot/grub/grub.conf"):
        call("grub", "Boot.Loader", "updateKernelEntry", (KVER, ""))

def preRemove():
    pass
