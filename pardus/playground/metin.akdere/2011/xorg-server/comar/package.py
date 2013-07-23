#!/usr/bin/python

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/usr/sbin/alternatives \
                --install   /usr/lib/xorg/modules/vnc  libvnc /var/empty  50")

def preRemove():
    #os.system("/usr/sbin/alternatives   --remove   libvnc /usr/lib/xorg/libvnc.so")
    pass
