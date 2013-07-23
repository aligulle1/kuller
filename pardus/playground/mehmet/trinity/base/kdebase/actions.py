#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
#

from pisi.actionsapi import kde
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools

KeepSpecial=["libtool"]
shelltools.export("HOME", get.workDIR())
WorkDir = "%s" % get.srcNAME()

def setup():
    # Fix automake and python detection
    pisitools.dosed("admin/cvs.sh", "automake\*1\.10\*", "automake*1.1[0-5]*")
    pisitools.dosed("admin/acinclude.m4.in", "KDE_CHECK_PYTHON_INTERN\(\"2.5", "KDE_CHECK_PYTHON_INTERN(\"%s" % get.curPYTHON().split("python")[1])
    shelltools.system("cp -Rp /usr/share/aclocal/libtool.m4 admin/libtool.m4.in")
    shelltools.system("cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh")
    kde.make("-f admin/Makefile.common")
    # the java test is problematic (see kde bug 100729) and
    # useless. All that's needed for java applets to work is
    # to have the 'java' executable in PATH.
    shelltools.export("DO_NOT_COMPILE", "kpersonalizer")

    #autotools.autoreconf("-vfi")
    kde.configure("--with-dpms \
                   --enable-dnssd \
                   --with-libaudit=yes \
                   --with-hal \
                   --with-ldap \
                   --with-cups \
                   --with-gl \
                   --with-ssl \
                   --with-samba \
                   --with-libusb \
                   --with-openexr \
                   --with-libraw1394 \
                   --with-hal \
                   --with-pam=yes \
                   --with-sudo-kdesu-backend \
                   --with-krb5auth \
                   --without-sensors \
                   --without-java \
                   --with-extra-libs=/usr/lib \
                   --with-extra-includes=/usr/include \
                   --enable-closure \
                   ")
                   #--enable-closure \

def build():
    pisitools.dosed("kcminit/Makefile", 
            "\-\-mode=link \$\(CXXLD\) \$\(AM_CXXFLAGS\) \$\(CXXFLAGS\) \$\(KDE_CXXFLAGS\) \$\(AM_LDFLAGS\)", 
            "--mode=link $(CXXLD) $(AM_CXXFLAGS) $(CXXFLAGS) $(KDE_CXXFLAGS) $(AM_LDFLAGS) /usr/kde/3.5/lib/libkdeui.so /usr/kde/3.5/lib/libkutils.so")
    pisitools.dosed("kdepasswd/Makefile",
            "\$\(CXXFLAGS\) \$\(KDE_CXXFLAGS\) \$\(kdepasswd_LDFLAGS\) \$\(LDFLAGS\)",
            "$(CXXFLAGS) $(KDE_CXXFLAGS) /usr/kde/3.5/lib/libkio.so $(kdepasswd_LDFLAGS) $(LDFLAGS)")
    kde.make("-j1")

def install():
    kde.install()
    #autotools.rawInstall("INSTALL_ROOT=%s" % get.installDIR())

    # kdm wants extra interest
    shelltools.cd("kdm")
    kde.install("GENKDMCONF_FLAGS=\"--no-old --no-backup --no-in-notice\" install")

    pisitools.remove("%s/share/templates/.source/emptydir" % get.kdeDIR())

    # Fix #730
    pisitools.remove("%s/share/autostart/ktip.desktop" % get.kdeDIR())

    # remove KDE's wallpapers, we've our own ;)
    pisitools.remove("%s/share/wallpapers/*" % get.kdeDIR())

    # remove kcontrol (we have TASMA), but not kinfocenter
    pisitools.remove("/usr/kde/3.5/bin/kinfocenter")
    pisitools.domove("/usr/kde/3.5/bin/kcontrol", "/usr/kde/3.5/bin/", "kinfocenter")
    pisitools.remove("/usr/kde/3.5/share/applications/kde/KControl.desktop")
    pisitools.remove("/usr/kde/3.5/share/applications/kde/Help.desktop")

    # Put kdmrc into /etc/X11/kdm, so it can be modified on live CDs
    pisitools.domove("/usr/kde/3.5/share/config/kdm/kdmrc", "/etc/X11/kdm/")
    pisitools.dosym("/etc/X11/kdm/kdmrc", "/usr/kde/3.5/share/config/kdm/kdmrc")

    # Use common Xsession script
    pisitools.remove("/usr/kde/3.5/share/config/kdm/Xsession")
    pisitools.dosym("/usr/lib/X11/xinit/Xsession", "/usr/kde/3.5/share/config/kdm/Xsession")

    # Remove shutdownkonq to replace it
    pisitools.remove("/usr/kde/3.5/share/apps/ksmserver/pics/shutdownkonq.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kdm/pics/shutdown.jpg")

    # artwork package provides these
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/kside.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/kside_tile.png")

    # Replace kicker's startup notification animation
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/disk*.png")

    # !!!
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/search-running.mng")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/main_corner_tl.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/resize_handle.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/search-gradient-topdown.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/right_triangle.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/search-tab-left.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/search-tab-right.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/main_corner_tr.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/left_triangle.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/icons/crystalsvg/48x48/apps/recently_used.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/search-gradient.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/menu_separator.png")
    pisitools.remove("/usr/kde/3.5/share/apps/kicker/pics/search-tab-center.png")
