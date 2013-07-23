#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

BuildNo = get.srcVERSION().split('_')[1]
WorkDir = "NVIDIA-Linux-x86-1.0-%s" % BuildNo
NoStrip = "/"

def build():
    shelltools.export("SYSSRC","/usr/src/linux")
    shelltools.cd("usr/src/nv")

    autotools.make("module")

def install():
    # Kernel driver
    pisitools.dodir("/lib/modules/%s/kernel/drivers/video" % get.curKERNEL())
    shelltools.copy("usr/src/nv/nvidia.ko","%s/lib/modules/%s/kernel/drivers/video/nvidia.ko" % (get.installDIR(),get.curKERNEL()))

    # X driver
    pisitools.dodir("/usr/lib/xorg/modules/drivers")
    shelltools.copy("usr/X11R6/lib/modules/drivers/nvidia_drv.so","%s/usr/lib/xorg/modules/drivers/nvidia_drv.so" % get.installDIR())

    # XvMC library
    pisitools.dodir("/usr/lib")
    shelltools.copy("usr/X11R6/lib/libXvMCNVIDIA*","%s/usr/lib" % get.installDIR())
    pisitools.dosym("/usr/lib/libXvMCNVIDIA.so.1.0.%s" % BuildNo,"/usr/lib/libXvMCNVIDIA.so")

    # Glx library & headers
    pisitools.dodir("/usr/lib/opengl/nvidia")

    pisitools.copytree("usr/include","%s/usr/lib/opengl/nvidia/include" % get.installDIR())
    pisitools.copytree("usr/lib", "%s/usr/lib/opengl/nvidia/lib" % get.installDIR())
    pisitools.copytree("usr/X11R6/lib/modules/extensions/", "%s/usr/lib/opengl/nvidia/extensions" % get.installDIR())

    pisitools.dosym("/usr/lib/opengl/nvidia/extensions/libglx.so.1.0.%s" % BuildNo,"/usr/lib/opengl/nvidia/extensions/libglx.so")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/libGLcore.so.1.0.%s" % BuildNo,"/usr/lib/opengl/nvidia/lib/libGLcore.so")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/libGLcore.so.1.0.%s" % BuildNo,"/usr/lib/opengl/nvidia/lib/libGLcore.so.1")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/libGL.so.1.0.%s" % BuildNo,"/usr/lib/opengl/nvidia/lib/libGL.so")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/libGL.so.1.0.%s" % BuildNo,"/usr/lib/opengl/nvidia/lib/libGL.so.1")

    # Our libc is TLS enabled so use TLS library
    pisitools.remove("/usr/lib/opengl/nvidia/lib/libnvidia-tls.so.1.0.%s" % BuildNo)
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/tls/libnvidia-tls.so.1.0.%s" % BuildNo,"/usr/lib/libnvidia-tls.so")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/tls/libnvidia-tls.so.1.0.%s" % BuildNo,"/usr/lib/libnvidia-tls.so.1")

    # Documentation
    pisitools.dodir("/usr/share/doc")
    shelltools.copytree("usr/share/doc","%s/usr/share/doc/nvidia-%s-%s" % (get.installDIR(),get.srcVERSION(),get.srcRELEASE()))
    shelltools.copytree("usr/share/man/","%s/usr/share/man" % get.installDIR())

    # nVIDIA utilities
    pisitools.dobin("usr/bin/nvidia-bug-report.sh")
    pisitools.dobin("usr/bin/nvidia-settings")
    pisitools.dobin("usr/bin/nvidia-xconfig")

    # libwfb.so replacement for Geforce FX8800 GPUs
    pisitools.insinto("/usr/lib/xorg/modules","usr/X11R6/lib/modules/libnvidia-wfb.so.1.0.9746")
    pisitools.dosym("/usr/lib/xorg/modules/libnvidia-wfb.so.1.0.9746","/usr/lib/xorg/modules/libwfb.so")
