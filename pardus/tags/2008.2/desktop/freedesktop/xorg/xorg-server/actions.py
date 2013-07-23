#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "."

xorgserver = "xorg-server-1.4.2"
mesa = "Mesa-7.0.4"

def setup():
    shelltools.cd(xorgserver)

    pisitools.dosed("configure.ac", r"^AC_SUBST\(\[libdir .*\]\)", "AC_SUBST([libdir])")
    autotools.autoreconf("-fi")
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
                         --with-mesa-source=%s/%s/ \
                         --with-dri-driver-path=/usr/lib/xorg/modules/dri \
                         --with-os-name=\"Pardus\" \
                         --with-os-vendor=\"TÜBİTAK, UEKAE\" \
                         --sysconfdir=/etc/X11 \
                         --localstatedir=/var \
                         --with-xkb-output=/var/lib/xkb \
                         --with-default-font-path=/usr/share/fonts/misc,/usr/share/fonts/dejavu,/usr/share/fonts/100dpi,/usr/share/fonts/75dpi,/usr/share/fonts/TTF,/usr/share/fonts/Type1" % (get.workDIR(), mesa))

def build():
    # prepare Mesa for compilation
    shelltools.cd(mesa)
    autotools.make('linux-dri-x86 OPTFLAGS="%s -fno-strict-aliasing -fvisibility=hidden -fPIC"' % get.CFLAGS())

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
    pisitools.dosym("libGLU.so.1.3.070004", "/usr/lib/libGLU.so.1.3")
    pisitools.dosym("libGLw.so.1.0.0", "/usr/lib/libGLw.so.1.0")

    # Moving libGL and friends for dynamic switching
    pisitools.domove("/usr/lib/libGL.so.1.2", "/usr/lib/xorg/std/lib")
    pisitools.domove("/usr/lib/xorg/modules/extensions/libglx.so", "/usr/lib/xorg/std/extensions")
    pisitools.domove("/usr/lib/xorg/modules/extensions/libdri.so", "/usr/lib/xorg/std/extensions")

    pisitools.domove("/usr/lib/xorg/modules/libwfb.so", "/usr/lib/xorg/std")

    for file in ("gl.h", "glx.h", "glext.h", "glxext.h"):
        pisitools.domove("/usr/include/GL/%s" % file, "/usr/lib/xorg/std/include")

    # Remove install dir paths
    pisitools.dosed("%s/usr/lib/pkgconfig/*.pc" % get.installDIR(), get.installDIR(), "")

    # Default cursor theme
    pisitools.dodir("/usr/share/cursors/xorg-x11/default")
    shelltools.echo("%s/usr/share/cursors/xorg-x11/default/index.theme" % get.installDIR(), "[Icon Theme]\nInherits=Jimmac")
