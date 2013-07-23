#!/usr/bin/python
import os

def postInstall():
    # add newly installed kernel/initramfs into grub.conf
    os.system("/sbin/update-grub")
