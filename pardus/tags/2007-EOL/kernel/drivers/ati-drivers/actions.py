#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

NoStrip = ["/lib/modules/"]
WorkDir = "."

def setup():
    shelltools.system("sh ati-driver-installer-8-02-x86.x86_64.run --extract .")

    pisitools.dosed("common/etc/ati/authatieventsd.sh", "/var/lib/xdm/authdir/authfiles", "/var/run/xauth")

def build():
    cur_dir = get.curDIR()

    # for gcc4 these must be converted to GCC4
    src = "%s/arch/x86/lib/modules/fglrx/build_mod/libfglrx_ip.a.GCC3" % (cur_dir)
    build_dir = "%s/common/lib/modules/fglrx/build_mod" % (cur_dir)
    shelltools.sym(src, "%s/%s" %(build_dir, "libfglrx_ip.a.GCC3"))

    shelltools.cd(build_dir)
    shelltools.system("sh make.sh")

def install():
    install_dir = get.installDIR()

    pisitools.dobin("arch/x86/usr/X11R6/bin/*")
    pisitools.dosbin("arch/x86/usr/sbin/*")
    pisitools.dosbin("common/usr/sbin/*")

    DIRS = {
            "common/etc":               "/",
            "common/usr/X11R6/include": "/usr",
            "arch/x86/usr/X11R6/lib":   "/usr/lib/opengl/ati",
            "common/usr/include/GL/":   "/usr/lib/opengl/ati/include",
            "common/usr/share":         "/usr"
            }

    for source, target in DIRS.items():
        pisitools.insinto(target, source)

    pisitools.insinto("/usr/lib/xorg/modules", "x710/usr/X11R6/lib/modules/*")

    pisitools.dosym("/usr/lib/opengl/ati/lib/modules/dri/fglrx_dri.so", "/usr/lib/xorg/modules/dri/fglrx_dri.so")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libGL.so.1.2", "/usr/lib/opengl/ati/lib/libGL.so.1")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libGL.so.1.2", "/usr/lib/opengl/ati/lib/libGL.so")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_pp.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_pp.so.1")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_pp.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_pp.so")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_gamma.so")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_dm.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_dm.so.1")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_dm.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_dm.so")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_tvout.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_tvout.so.1")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_tvout.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_tvout.so")

    # links to /usr/lib
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_pp.so.1.0", "/usr/lib/libfglrx_pp.so")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_pp.so.1.0", "/usr/lib/libfglrx_pp.so.1")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1.0", "/usr/lib/libfglrx_gamma.so")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1.0", "/usr/lib/libfglrx_gamma.so.1")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_dm.so.1.0", "/usr/lib/libfglrx_dm.so")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_dm.so.1.0", "/usr/lib/libfglrx_dm.so.1")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_tvout.so.1.0", "/usr/lib/libfglrx_tvout.so")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_tvout.so.1.0", "/usr/lib/libfglrx_tvout.so.1")

    # remove previous libGL links
    pisitools.remove("/usr/lib/libGL.so")
    pisitools.remove("/usr/lib/libGL.so.1")

    # compability links
    pisitools.dosym("/usr/", "/usr/X11R6")
    # PiSi BUG: That destination is directory before, so pisi cant handle that, postInstall script used instead
    pisitools.dosym("/usr/lib/xorg/modules", "/usr/lib/modules")

    # copy compiled kernel module
    pisitools.insinto("/lib/modules/%s/kernel/drivers/char/drm" % get.curKERNEL(), "common/lib/modules/fglrx/fglrx.%s.ko" % get.curKERNEL(), "fglrx.ko")

    # remove static libs
    pisitools.remove("/usr/lib/opengl/ati/lib/*.a")
    pisitools.remove("/usr/lib/xorg/modules/*.a")

    # No kitty
    pisitools.removeDir("/usr/share/gnome")
