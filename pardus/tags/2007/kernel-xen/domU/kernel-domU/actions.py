#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005, 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "linux-2.6.16"
EXTRAVERSION = "29"
NoStrip = "/"

def setup():
    # Branding
    if EXTRAVERSION is not None:
        pisitools.dosed("Makefile", "EXTRAVERSION =.*", "EXTRAVERSION = .%s-%s-domU" % (EXTRAVERSION, get.srcRELEASE()))
    else:
        pisitools.dosed("Makefile", "EXTRAVERSION =.*", "EXTRAVERSION = -%s" % get.srcRELEASE())

    autotools.make("oldconfig")

def build():
    autotools.make()

def install():
    autotools.rawInstall("INSTALL_MOD_PATH=%s/" % get.installDIR(), "modules_install")

    suffix = "%s-%s-domU" % (get.srcVERSION(), get.srcRELEASE())

    # remove wrong symlinks
    pisitools.remove("/lib/modules/%s/source" % suffix)
    pisitools.remove("/lib/modules/%s/build" % suffix)

    # create symlinks
    pisitools.dosym("/usr/src/linux-%s/" % suffix, "/lib/modules/%s/source" % suffix)
    pisitools.dosym("/usr/src/linux-%s/" % suffix, "/lib/modules/%s/build" % suffix)

    # insert System.map and bzImage
    pisitools.insinto("/boot/", "System.map", "System.map-%s" % suffix)
    pisitools.insinto("/boot/", "vmlinux", "kernel-%s" % suffix)

    # prepare kernel for module compiliation
    autotools.make("clean")
    autotools.make("modules_prepare")

    # cp source to installDIR for kernel-source package
    pisitools.dodir("/usr/src")

    shelltools.copytree("../%s/" % WorkDir, "%s/usr/src/linux-%s/" % (get.installDIR(), suffix))

    pisitools.dosym("/usr/src/linux-%s/" % suffix, "/usr/src/linux")

    # generate mkinitramfs
    shelltools.system("/sbin/mkinitramfs kernel=%s --full --root-dir=%s --output=/%s/boot" % (suffix, get.installDIR(), get.installDIR()))
