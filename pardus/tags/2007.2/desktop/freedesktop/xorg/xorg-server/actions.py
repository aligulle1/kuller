#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

xorgserver = "xorg-server-1.3.0.0"
mesa = "Mesa-7.0"

def setup():
    shelltools.cd(xorgserver)

    libtools.libtoolize("--copy --force")
    autotools.autoreconf()
    autotools.automake()

    autotools.configure("--enable-ipv6 \
                        --enable-xvfb \
                        --enable-xnest \
                        --enable-install-libxf86config \
                        --enable-dri \
                        --enable-xorg \
                        --enable-glx-tls \
                        --disable-xorgcfg \
                        --disable-xprint \
                        --disable-static \
                        --with-pic \
                        --enable-composite \
                        --with-mesa-source=%s/xorg-server-7.2/%s/ \
                        --with-dri-driver-path=/usr/lib/xorg/modules/dri \
                        --with-os-name=\"Pardus\" \
                        --with-os-vendor=\"TÜBİTAK, UEKAE\" \
                        --sysconfdir=/etc/X11 \
                        --localstatedir=/var \
                        --with-default-font-path=/usr/share/fonts/misc,/usr/share/fonts/dejavu,/usr/share/fonts/100dpi,/usr/share/fonts/75dpi,/usr/share/fonts/TTF,/usr/share/fonts/Type1" % (get.workDIR(), mesa))

def build():
    # prepare Mesa for compilation
    shelltools.cd(mesa)
    autotools.make("linux-dri-x86")

    shelltools.cd("../%s" % xorgserver)
    autotools.make()

def install():
    shelltools.cd(xorgserver)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("../%s/" % mesa)
    autotools.rawInstall("INSTALL_DIR=%s/usr DRI_DRIVER_INSTALL_DIR=%s/usr/lib/xorg/modules/dri INCLUDE_DIR=%s/usr/include" % 
        (get.installDIR(), get.installDIR(), get.installDIR()))

    # Create glxinfo/gears
    shelltools.cd("progs/xdemos/")
    autotools.make("glxinfo")
    autotools.make("glxgears")

    pisitools.insinto("/usr/bin", "glxinfo")
    pisitools.insinto("/usr/bin", "glxgears")

    # Don't install private headers
    pisitools.remove("/usr/include/GL/GLw*P.h")

    # Create needed symlinks
    pisitools.dosym("libGLU.so.1.3.070100", "/usr/lib/libGLU.so.1.3")
    pisitools.dosym("libGLw.so.1.0.0", "/usr/lib/libGLw.so.1.0")

    # Moving libGL and friends for dynamic switching
    pisitools.dodir("/usr/lib/opengl/lib")
    pisitools.dodir("/usr/lib/opengl/extensions")
    pisitools.dodir("/usr/lib/opengl/include")

    for file in shelltools.ls("%s/usr/lib/libGL.so*" % get.installDIR()):
        pisitools.domove(file.replace(get.installDIR(), ""), "/usr/lib/opengl/xorg-x11/lib/")

    pisitools.domove("/usr/lib/libGL.la", "/usr/lib/opengl/xorg-x11/lib/")
    pisitools.domove("/usr/lib/libGL.a", "/usr/lib/opengl/xorg-x11/lib/")

    for file in shelltools.ls("%s/usr/lib/xorg/modules/extensions/libglx*" % get.installDIR()):
        pisitools.domove(file.replace(get.installDIR(), ""), "/usr/lib/opengl/xorg-x11/extensions/")

    for file in ("gl.h", "glx.h", "glext.h", "glxext.h"):
        pisitools.domove("/usr/include/GL/%s" % file, "/usr/lib/opengl/xorg-x11/include")

    # Default cursor theme
    pisitools.dodir("/usr/share/cursors/xorg-x11/default")
    shelltools.echo("%s/usr/share/cursors/xorg-x11/default/index.theme" % get.installDIR(), "[Icon Theme]\nInherits=Jimmac")

    # Workaround for liveCD
    pisitools.removeDir("/usr/share/X11/xkb/compiled/")
    pisitools.dosym("/tmp", "/usr/share/X11/xkb/compiled")
    pisitools.dosym("/usr/share/X11/xkb", "/etc/X11/xkb")
