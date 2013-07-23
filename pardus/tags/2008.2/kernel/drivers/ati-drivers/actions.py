#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

import os

NoStrip = ["/lib/modules/"]
WorkDir = "."

def setup():
    shelltools.system("sh ati-driver-installer-%s-x86.x86_64.run --extract ." % get.srcVERSION().replace(".", "-"))

    pisitools.dosed("common/lib/modules/fglrx/build_mod/make.sh", r"^linuxincludes=.*", "linuxincludes=/lib/modules/%s/build/include" % get.curKERNEL())
    pisitools.dosed("common/etc/ati/authatieventsd.sh", "/var/lib/xdm/authdir/authfiles", "/var/run/xauth")

def build():
    cur_dir = get.curDIR()

    src = "%s/arch/x86/lib/modules/fglrx/build_mod/libfglrx_ip.a.GCC4" % (cur_dir)
    build_dir = "%s/common/lib/modules/fglrx/build_mod" % (cur_dir)
    shelltools.sym(src, "%s/%s" %(build_dir, "libfglrx_ip.a.GCC4"))

    shelltools.cd(build_dir)
    shelltools.system("sh make.sh")

def install():
    pisitools.dobin("arch/x86/usr/X11R6/bin/*")
    pisitools.dobin("common/usr/X11R6/bin/*")
    pisitools.dosbin("arch/x86/usr/sbin/*")
    pisitools.dosbin("common/usr/sbin/*")

    DIRS = {
            "common/usr/share/doc/fglrx/examples/etc/acpi/events":  "/etc/acpi",
            "common/etc":               "/",
            "common/usr/X11R6/include": "/usr",
            "arch/x86/usr/X11R6/lib/*": "/usr/lib",
            "arch/x86/usr/lib/*":       "/usr/lib",
            "common/usr/include/GL/":   "/usr/lib/xorg/fglrx/include",
            "common/usr/share":         "/usr"
            }

    for source, target in DIRS.items():
        pisitools.insinto(target, source)

    pisitools.domove("/usr/lib/modules", "/usr/lib/xorg")
    pisitools.insinto("/usr/lib/xorg/modules", "x710/usr/X11R6/lib/modules/*")

    pisitools.domove("/usr/lib/libGL.so.1.2", "/usr/lib/xorg/fglrx/lib")
    pisitools.domove("/usr/lib/xorg/modules/extensions", "/usr/lib/xorg/fglrx")

    pisitools.dosym("libfglrx_dm.so.1.0", "/usr/lib/libfglrx_dm.so.1")
    pisitools.dosym("libfglrx_dm.so.1", "/usr/lib/libfglrx_dm.so")

    pisitools.dosym("libfglrx_gamma.so.1.0", "/usr/lib/libfglrx_gamma.so.1")
    pisitools.dosym("libfglrx_gamma.so.1", "/usr/lib/libfglrx_gamma.so")

    pisitools.dosym("libfglrx_pp.so.1.0", "/usr/lib/libfglrx_pp.so.1")
    pisitools.dosym("libfglrx_pp.so.1", "/usr/lib/libfglrx_pp.so")

    pisitools.dosym("libfglrx_tvout.so.1.0", "/usr/lib/libfglrx_tvout.so.1")
    pisitools.dosym("libfglrx_tvout.so.1", "/usr/lib/libfglrx_tvout.so")

    pisitools.dosym("libAMDXvBA.so.1.0", "/usr/lib/libAMDXvBA.so.1")
    pisitools.dosym("libAMDXvBA.so.1", "/usr/lib/libAMDXvBA.so")

    pisitools.dosym("libXvBAW.so.1.0", "/usr/lib/libXvBAW.so.1")
    pisitools.dosym("libXvBAW.so.1", "/usr/lib/libXvBAW.so")

    # compability links
    pisitools.dosym("/usr", "/usr/X11R6")
    pisitools.dosym("xorg/modules", "/usr/lib/modules")

    # copy compiled kernel module
    pisitools.insinto("/lib/modules/%s/kernel/drivers/char/drm" % get.curKERNEL(), "common/lib/modules/fglrx/fglrx.%s.ko" % get.curKERNEL(), "fglrx.ko")

    # remove static libs
    pisitools.remove("/usr/lib/*.a")
    pisitools.remove("/usr/lib/xorg/modules/*.a")

    # No kitty
    pisitools.removeDir("/usr/share/applnk")
    pisitools.removeDir("/usr/share/gnome")

    pisitools.domove("/usr/share/icons/ccc_large.xpm", "/usr/share/pixmaps", "amdcccle.xpm")
    pisitools.removeDir("/usr/share/icons")

    # Fix file permissions
    exec_file_suffixes = (".sh", ".so")
    exec_dir_suffixes = ("/bin", "/sbin", "/lib")

    for root, dirs, files in os.walk(get.installDIR()):
        for name in files:
            filePath = os.path.join(root, name)
            if root.endswith(exec_dir_suffixes) \
                or name.endswith(exec_file_suffixes):
                shelltools.chmod(filePath, 0755)
            else:
                shelltools.chmod(filePath, 0644)
