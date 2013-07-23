#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.


from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

NoStrip = "/"
WorkDir = "."

def setup():
    shelltools.system("sh ati-driver-installer-8.34.8-x86.x86_64.run --extract .")

def build():
    cur_dir = get.curDIR()
    src = "%s/arch/x86/lib/modules/fglrx/build_mod/libfglrx_ip.a.GCC3" % (cur_dir)
    build_dir = "%s/common/lib/modules/fglrx/build_mod" % (cur_dir)
    shelltools.sym(src, "%s/%s" %(build_dir, "libfglrx_ip.a.GCC3"))

    shelltools.cd(build_dir)
    shelltools.system("sh make.sh")

def install():
    install_dir = get.installDIR()

    DIRS = {"common/etc": "etc",
            "common/usr/X11R6/include": "usr/",
            "arch/x86/usr/X11R6/bin": "opt/ati/bin",
            "arch/x86/usr/sbin": "opt/ati/sbin",
            "arch/x86/usr/X11R6/lib": "usr/lib/opengl/ati/lib",
            "common/usr/include/GL/": "usr/lib/opengl/ati/include/GL",
            "common/usr/share": "usr/share"}

    pisitools.dodir("/opt/ati")
    pisitools.dodir("/usr")
    pisitools.dodir("/usr/lib/opengl/ati")
    pisitools.dodir("/usr/lib/opengl/ati/include")
    for source in DIRS:
        target = DIRS[source]
        shelltools.copy(source, "%s/%s" %(install_dir, target))

    pisitools.insinto("/opt/ati/bin", "x710/usr/X11R6/bin/*")
    pisitools.insinto("/opt/ati/bin", "x690/usr/X11R6/bin/*")
    pisitools.insinto("/usr/lib/xorg/modules", "x710/usr/X11R6/lib/modules/*")

    #
    pisitools.dosym("/usr/lib/opengl/ati/lib/modules/dri/atiogl_a_dri.so", "/usr/lib/xorg/modules/dri/atiogl_a_dri.so")
    pisitools.dosym("/usr/lib/opengl/ati/lib/modules/dri/fglrx_dri.so", "/usr/lib/xorg/modules/dri/fglrx_dri.so")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libGL.so.1.2", "/usr/lib/opengl/ati/lib/libGL.so.1")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libGL.so.1.2", "/usr/lib/opengl/ati/lib/libGL.so")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_pp.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_pp.so.1")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_pp.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_pp.so")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_gamma.so")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_dm.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_dm.so.1")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_dm.so.1.0", "/usr/lib/opengl/ati/lib/libfglrx_dm.so")

    # links to /usr/lib
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_pp.so.1.0", "/usr/lib/libfglrx_pp.so")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_pp.so.1.0", "/usr/lib/libfglrx_pp.so.1")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1.0", "/usr/lib/libfglrx_gamma.so")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_gamma.so.1.0", "/usr/lib/libfglrx_gamma.so.1")

    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_dm.so.1.0", "/usr/lib/libfglrx_dm.so")
    pisitools.dosym("/usr/lib/opengl/ati/lib/libfglrx_dm.so.1.0", "/usr/lib/libfglrx_dm.so.1")

    # remove previous libGL links
    pisitools.remove("/usr/lib/libGL.so")
    pisitools.remove("/usr/lib/libGL.so.1")

    # binaries and modules symlinks
    pisitools.dosym("/opt/ati/bin/aticonfig", "/usr/bin/aticonfig")
    pisitools.dosym("/opt/ati/bin/fgl_glxgears", "/usr/bin/fgl_glxgears")
    pisitools.dosym("/opt/ati/bin/fglrx_xgamma", "/usr/bin/fglrx_xgamma")
    pisitools.dosym("/opt/ati/bin/fglrxinfo", "/usr/bin/fglrxinfo")
    pisitools.dosym("/opt/ati/bin/fireglcontrolpanel", "/usr/bin/fireglcontrolpanel")
    pisitools.dosym("/opt/ati/sbin/atieventsd", "/usr/sbin/atieventsd")

    # compability links
    pisitools.dosym("/usr/", "/usr/X11R6")
    pisitools.dosym("/usr/lib/xorg/modules", "/usr/lib/modules")

    # copy compiled kernel module
    pisitools.insinto("/lib/modules/%s/kernel/drivers/char/drm" % get.curKERNEL(), "common/lib/modules/fglrx/fglrx.%s.ko" % get.curKERNEL(), "fglrx.ko")
    pisitools.insinto("/lib/modules/%s/kernel/drivers/char/drm" % get.curKERNEL(), "common/lib/modules/fglrx/fglrx_agp.%s.ko" % get.curKERNEL(), "fglrx_agp.ko")

    # No kitty
    pisitools.removeDir("/usr/share/gnome")
