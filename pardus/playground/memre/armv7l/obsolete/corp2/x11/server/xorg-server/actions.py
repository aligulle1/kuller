# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.chmod("hw/vnc/symlink-vnc.sh")

    cache = [ "ac_cv_header_linux_apm_bios_h=no",
              "ac_cv_file__usr_share_sgml_X11_defs_ent=no" ]

    autotools.environment["LDFLAGS"] = "%(LDFLAGS)s -ldl" % autotools.environment

    autotools.autoreconf("-fiv")
    autotools.configure('--enable-install-libxf86config \
                         --enable-aiglx \
                         --enable-glx-tls \
                         --enable-composite \
                         --enable-record \
                         --enable-dri \
                         --enable-dri2 \
                         --disable-unit-tests \
                         --enable-config-dbus \
                         --enable-config-hal \
                         --enable-xfree86-utils \
                         --enable-xorg \
                         --disable-xcliplist \
                         --enable-vnc \
                         --disable-dmx \
                         --enable-xvfb \
                         --disable-xnest \
                         --enable-kdrive \
                         --disable-kdrive-vesa \
                         --enable-xephyr \
                         --disable-xsdl \
                         --disable-xfake \
                         --disable-xfbdev \
                         --with-pic \
                         --without-dtrace \
                         --without-int10 \
                         --with-os-name="Pardus" \
                         --with-os-vendor="TÜBİTAK, UEKAE" \
                         --with-builderstring="Package: %s" \
                         --with-fontdir=/usr/share/fonts \
                         --with-default-font-path=catalogue:/etc/X11/fontpath.d,built-ins \
                         --with-xkb-output=/var/lib/xkb \
                         --with-dri-driver-path=/usr/lib/xorg/modules/dri \
                         --localstatedir=/var \
                         PCI_TXT_IDS_DIR=/usr/share/X11/pci \
                         ' % get.srcTAG(), cache=cache)
                         # FIXME: --enable-xcalibrate \
                         #        --enable-dmx \

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/etc/X11/fontpath.d")
    pisitools.dodir("/usr/share/X11/pci")

    pisitools.remove("/usr/lib/xorg/modules/*.la")
    pisitools.remove("/usr/lib/xorg/modules/*/*.la")

    # Remove empty dir
    pisitools.removeDir("/var/log")

    # Move glx and dri modules for dynamic switching
    pisitools.domove("/usr/lib/xorg/modules/extensions/libglx.so", "/usr/lib/xorg/std/extensions")
    pisitools.domove("/usr/lib/xorg/modules/extensions/libdri.so", "/usr/lib/xorg/std/extensions")
