#!/usr/bin/python

import os

def postInstall():
    try:
        os.makedirs("/etc/udev/devices")
    except OSError:
        pass

    os.system("mknod -m 0600 /etc/udev/devices/nvidia0 c 195 0")
    os.system("mknod -m 0600 /etc/udev/devices/nvidia1 c 195 1")
    os.system("mknod -m 0600 /etc/udev/devices/nvidia2 c 195 2")
    os.system("mknod -m 0600 /etc/udev/devices/nvidia3 c 195 3")
    os.system("mknod -m 0600 /etc/udev/devices/nvidiactl c 195 255")

    os.system("mknod /dev/nvidia0 c 195 0")
    os.system("mknod /dev/nvidiactl c 195 255")
