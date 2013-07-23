#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "NVIDIA-Linux-x86-%s" % get.srcVERSION()
NoStrip = "/"

def build():
    shelltools.export("SYSSRC","/lib/modules/%s/source" % get.curKERNEL())
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
    pisitools.dosym("/usr/lib/libXvMCNVIDIA.so.%s" % get.srcVERSION(),"/usr/lib/libXvMCNVIDIA.so")

    # Glx library & headers
    pisitools.dodir("/usr/lib/opengl/nvidia")

    pisitools.copytree("usr/include","%s/usr/lib/opengl/nvidia/include" % get.installDIR())
    pisitools.copytree("usr/lib", "%s/usr/lib/opengl/nvidia/lib" % get.installDIR())
    pisitools.copytree("usr/X11R6/lib/modules/extensions/", "%s/usr/lib/opengl/nvidia/extensions" % get.installDIR())

    pisitools.dosym("/usr/lib/opengl/nvidia/extensions/libglx.so.%s" % get.srcVERSION(),"/usr/lib/opengl/nvidia/extensions/libglx.so")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/libGLcore.so.%s" % get.srcVERSION(),"/usr/lib/opengl/nvidia/lib/libGLcore.so")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/libGLcore.so.%s" % get.srcVERSION(),"/usr/lib/opengl/nvidia/lib/libGLcore.so.1")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/libGL.so.%s" % get.srcVERSION(),"/usr/lib/opengl/nvidia/lib/libGL.so")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/libGL.so.%s" % get.srcVERSION(),"/usr/lib/opengl/nvidia/lib/libGL.so.1")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/libGL.so.%s" % get.srcVERSION(),"/usr/lib/opengl/nvidia/lib/libGL.so.1.2")

    # Our libc is TLS enabled so use TLS library
    pisitools.remove("/usr/lib/opengl/nvidia/lib/libnvidia-tls.so.%s" % get.srcVERSION())
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/tls/libnvidia-tls.so.%s" % get.srcVERSION(),"/usr/lib/libnvidia-tls.so")
    pisitools.dosym("/usr/lib/opengl/nvidia/lib/tls/libnvidia-tls.so.%s" % get.srcVERSION(),"/usr/lib/libnvidia-tls.so.1")

    # nVIDIA utilities
    pisitools.dobin("usr/bin/nvidia-bug-report.sh")
    pisitools.dobin("usr/bin/nvidia-settings")
