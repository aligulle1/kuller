#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
tigervnc_workdir = "%s-%s" % (get.srcNAME(), get.srcVERSION())
xorgserver_workdir = "xorg-server-1.9.5"


def setup():
    shelltools.export("AUTOPOINT", "true")

    # xorg-server package does not contain unix/xserver/hw/vnc, but tigervnc does, so append it with the copied context
    shelltools.copytree("%s/%s/unix/xserver/hw/vnc" % (get.workDIR(), tigervnc_workdir), "%s/%s/hw/" %(get.workDIR(), xorgserver_workdir))
    shelltools.unlinkDir("%s/%s/unix/xserver/hw" % (get.workDIR(), tigervnc_workdir))
    shelltools.copy("%s/%s/*" %(get.workDIR(), xorgserver_workdir), "%s/%s/unix/xserver/" % (get.workDIR(), tigervnc_workdir))

    shelltools.cd(tigervnc_workdir)
    pisitools.dosed("configure.ac", "AM_GNU_GETTEXT_VERSION.*", "AM_GNU_GETTEXT_VERSION([0.18.1])")
    autotools.autoreconf("-fiv")
    autotools.configure("--with-system-jpeg \
                         --enable-nls \
                         --disable-static")

    shelltools.cd("unix/xserver")
    autotools.autoreconf("-fiv")

    #Mostly try to keep pace with our xorg-server configuration
    autotools.configure("--enable-install-libxf86config \
                         --enable-aiglx \
                         --enable-glx-tls \
                         --enable-composite \
                         --enable-record \
                         --enable-dri \
                         --enable-dri2 \
                         --enable-glx \
                         --enable-glx-tls \
                         --disable-xorg \
                         --disable-xnest \
                         --disable-xvfb \
                         --disable-xwin \
                         --disable-dmx \
                         --disable-xephyr \
                         --disable-kdrive \
                         --disable-static \
                         --disable-xinerama \
                         --disable-composite \
                         --disable-config-dbus \
                         --disable-config-hal \
                         --disable-config-udev \
                         --with-pic \
                         --with-default-font-path=catalogue:/etc/X11/fontpath.d,built-ins \
                         --with-dri-driver-path=/usr/lib/xorg/modules/dri")


def build():
    #Build TigerVNC viewer client
    shelltools.cd(tigervnc_workdir)
    autotools.make()

    #Build TigerVNC server
    shelltools.cd("unix/xserver")
    autotools.make()

    #Build icons
    shelltools.cd("../../media")
    autotools.make()

    #Build TigerVNC java viewer
    shelltools.cd("../java/src/com/tigervnc/vncviewer")
    autotools.make()

def install():
    pisitools.dodir("/usr/share/vnc/classes")

    shelltools.cd("%s/unix" % tigervnc_workdir)
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("../LICENCE.TXT")

    #Install server
    shelltools.cd("xserver/hw/vnc")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Move libvnc.so for dynamic switching
    pisitools.domove("/usr/lib/xorg/modules/extensions/libvnc.so", "/usr/lib/tigervnc/modules/extensions")
    pisitools.rename("/usr/bin/Xvnc", "Xvnc-tigervnc")

    #Install icons
    shelltools.cd("../../../../media/icons")
    for size in [16, 24, 48]:
        pisitools.insinto("/usr/share/icons/hicolor/%sx%s/apps" % (size, size), "tigervnc_%s.png" % size, "tigervnc.png")

    #Install Java stuff
    shelltools.cd("../../java/src/com/tigervnc/vncviewer")
    autotools.rawInstall("INSTALL_DIR=%s/usr/share/vnc/classes" % get.installDIR())
