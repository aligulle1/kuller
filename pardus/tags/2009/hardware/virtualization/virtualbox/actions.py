#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "VirtualBox-%s_OSE" % get.srcVERSION()

installDir = "/usr/lib/virtualbox"
outDir = "out/linux.x86/release/bin"
XorgVersion = "16"

def setup():
    autotools.rawConfigure("--disable-kmods \
                            --enable-hardening \
                            --with-gcc=%s \
                            --with-g++=%s \
                            --with-qt-dir=/usr/qt/4" % (get.CC(), get.CXX()))

def build():
    shelltools.system("source env.sh && kmk")

    # Remove tests
    for tstfile in shelltools.ls("%s/tst*" % outDir):
        shelltools.unlink(tstfile)

def install():
    apps = ("VirtualBox", "VBoxSDL", "VBoxHeadless", "VBoxManage")
    files = apps + \
            ("VBoxSVC", "VBoxXPCOMIPCD", "VBoxBFE", "VBoxTunctl", \
             "VBoxNetAdpCtl", "VBoxNetDHCP", \
             "*.sh", "*.so", "*.r0", "*.gc", "components", "nls")

    for _file in files:
        pisitools.insinto(installDir, "%s/%s" % (outDir, _file))

    # Symlinks
    for link in apps + ("VBoxVRDP",):
        pisitools.dosym("%s/VBox.sh" % installDir, "/usr/bin/%s" % link)

    pisitools.dosym("%s/VBoxTunctl" % installDir, "/usr/bin/VBoxTunctl")

    pisitools.dodir("/etc/vbox")
    shelltools.echo("%s/etc/vbox/vbox.cfg" % get.installDIR(), "INSTALL_DIR=%s" % installDir)

    # Desktop file
    pisitools.insinto("/usr/share/applications/","%s/VirtualBox.desktop" % outDir)
    pisitools.insinto("/usr/share/pixmaps/","%s/VBox.png" % outDir)

    # Guest additions
    pisitools.dobin("%s/additions/VBoxClient" % outDir)
    pisitools.dosbin("%s/additions/VBoxControl" % outDir)
    pisitools.dosbin("%s/additions/VBoxService" % outDir)
    pisitools.insinto("/sbin", "%s/additions/mountvboxsf" % outDir, "mount.vboxsf")

    pisitools.insinto("/etc/X11/Xsession.d", "src/VBox/Additions/x11/Installer/98vboxadd-xclient", "98-vboxclient.sh")
    pisitools.insinto("/usr/bin", "src/VBox/Additions/x11/Installer/VBoxRandR.sh", "VBoxRandR")

    pisitools.dolib("%s/additions/VBoxOGL*" % outDir)
    pisitools.dosym("/usr/lib/VBoxOGL.so", "/usr/lib/xorg/modules/dri/vboxvideo_dri.so")

    pisitools.insinto("/usr/share/X11/pci", "src/VBox/Additions/x11/Installer/vboxvideo.ids")
    pisitools.insinto("/usr/lib/xorg/modules/drivers", "%s/additions/vboxvideo_drv_%s.so" % (outDir, XorgVersion), "vboxvideo_drv.so")
    pisitools.insinto("/usr/lib/xorg/modules/input",   "%s/additions/vboxmouse_drv_%s.so" % (outDir, XorgVersion), "vboxmouse_drv.so")

    pisitools.insinto("/usr/share/hal/fdi/policy/10osvendor", "src/VBox/Additions/linux/installer/90-vboxguest.fdi")
