#!/usr/bin/python

import os


def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives \
                --install   /usr/lib/xorg/modules/vnc  libvnc \
                            /usr/lib/tigervnc/modules/extensions/libvnc.so  80")

def preRemove():
    os.system("/usr/sbin/alternatives   --remove  libvnc /usr/lib/tigervnc/modules/extensions/libvnc.so")
