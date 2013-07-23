#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import kerneltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import re

WorkDir = "git"
NoStrip = ["/"]

# I had to add these methods to here.
def __getFlavour():
    flavour = ""
    try:
        flavour = get.srcNAME().split("kernel-")[1]
    except IndexError:
        pass

    return flavour

def __getModuleFlavour():
    for fl in [_f for _f in __getAllSupportedFlavours() if "-" in _f]:
        try:
            if fl.split("-")[1] == get.srcNAME().split("-")[1]:
                return fl
        except IndexError:
            pass

    return "kernel"

def __getSuffix():
    suffix = "%s-%s" % (get.srcVERSION(), get.srcRELEASE())
    if __getFlavour():
        suffix += "-%s" % __getFlavour()

    return suffix

def __getExtraVersion():
    extraversion = ""
    try:
        # if successful, this is something like:
        # .1 for 2.6.30.1
        # _rc8 for 2.6.30_rc8
        extraversion = re.split("2.[0-9].[0-9]{2}([._].*)", get.srcVERSION())[1]
    except IndexError:
        # e.g. if version == 2.6.30
        pass

    extraversion += "-%s" % get.srcRELEASE()

    # Append pae, default, rt, etc. to the extraversion if available
    if __getFlavour():
        extraversion += "-%s" % __getFlavour()

    return extraversion

def setup():
    shelltools.system('find . -name "*.orig" | xargs rm -f')
    pisitools.dosed("Makefile", "EXTRAVERSION =.*", "EXTRAVERSION = %s" % __getExtraVersion())
    shelltools.copy("configs/kernel-armv7a-config", ".config")

def build():
    extra_config = ["CONFIG_DEBUG_SECTION_MISMATCH=y", "CONFIG_DEBUG_INFO=y"]

    crosstools.make("%s ARCH=arm CROSS_COMPILE=%s-" % (" ".join(extra_config), crosstools.environment["target"]), cleanFlags=True)

    shelltools.system("%(OBJCOPY)s -O binary -R .note -R .comment -S arch/arm/boot/compressed/vmlinux linux.bin" % crosstools.environment)
    shelltools.system('mkimage \
                       -A arm \
                       -O linux \
                       -T kernel \
                       -C none \
                       -a 0x80008000 -e 0x80008000 \
                       -n "Pardus-ARM Kernel for OMAP3530" \
                       -d linux.bin arch/arm/boot/uImage')

    """
    ·   mkimage -A arm -O linux -T kernel -C gzip \
    ·   ·   -a 0 -e 0 -n "Linux Kernel Image" \
    ·   ·   -d linux.bin.gz uImage

    ·   tools/mkimage -A arch -O os -T type -C comp -a addr -e ep \
    ·   ·         -n name -d data_file image
    ·     -A ==> set architecture to 'arch'
    ·     -O ==> set operating system to 'os'
    ·     -T ==> set image type to 'type'
    ·     -C ==> set compression type 'comp'
    ·     -a ==> set load address to 'addr' (hex)
    ·     -e ==> set entry point to 'ep' (hex)
    ·     -n ==> set image name to 'name'
    ·     -d ==> use image data from 'datafile'
    """

    """
    # for making initrd
    mkimage \
       -A arm \
       -O linux \
       -T ramdisk \
       -C none \
       -a 0x81600000 -e 0x81600000 \
       -n "Pardus-ARM initramfs" \
       -d initramfs_ \
       initramfs
    """
    # console=ttyS2,115200n8 root=/dev/mmcblk0p2 rw rootfstype=ext3 rootdelay=3 noinitrd
    # mmcinit; fatload mmc 0 80000000 uimage; bootm 80000000

def install():
    suffix = __getSuffix()
    arch = "arm"

    # Install the modules into /lib/modules
    if re.search("CONFIG_MODULES=y", open(".config", "r").read().strip()):
        # Install the modules into /lib/modules
        crosstools.rawInstall("ARCH=arm INSTALL_MOD_PATH=%s" % get.installDIR(),
                              "modules_install")

        # Install Module.symvers and System.map
        pisitools.insinto("/lib/modules/%s/" % suffix, "System.map")
        pisitools.insinto("/lib/modules/%s/" % suffix, "Module.symvers")

        # Remove wrong symlinks
        pisitools.remove("/lib/modules/%s/source" % suffix)
        pisitools.remove("/lib/modules/%s/build" % suffix)

    # Install kernel image
    pisitools.insinto("/boot/", "arch/%s/boot/uImage" % arch, "uimage") # u-boot kernel image
    pisitools.insinto("/boot/", "arch/%s/boot/zImage" % arch, "kernel-%s" % suffix) # compressed kernel image

    # Dump kernel version into /etc/kernel/
    kerneltools.dumpVersion()

    # Install kernel headers needed for out-of-tree module compilation
    # You can provide a list of extra directories from which to grab *.h files.
    kerneltools.installHeaders(extra=["drivers/media/dvb/dvb-core",
                                      "drivers/media/dvb/frontends",
                                      "drivers/media/video"])

    # Drop /usr/include/scsi directory as it's shipped within glibc
    kerneltools.installLibcHeaders(excludes=["scsi"], extra_param="ARCH=arm")

    # Install kernel source
    #kerneltools.installSource()

    # Clean module-init-tools related stuff
    # kerneltools.cleanModuleFiles()

    # Build and install the new 'perf' tool
    #crosstools.make('V=1 -C tools/perf perf \
                    #CFLAGS="%s" \
                    #LDFLAGS="%s" \
                    #ARCH=arm CROSS_COMPILE=%s-' % \
                    #(get.CFLAGS(), get.LDFLAGS(), _target))
    #pisitools.insinto("/usr/bin", "tools/perf/perf", "perf.%s-%s" % (get.srcNAME(), get.srcVERSION()))
    #crosstools.install("-C tools/perf/Documentation install-man mandir=%s/usr/share/man" % get.installDIR())

