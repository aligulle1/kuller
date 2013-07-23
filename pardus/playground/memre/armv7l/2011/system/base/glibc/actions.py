#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

WorkDir = "glibc-2.12-26-g9a98163"
#WorkDir = "glibc-2.12.1"

if get.ARCH() == "arm":
    defaultflags = "-g -U_FORTIFY_SOURCE -fno-strict-aliasing"
else:
    defaultflags = "-O3 -g -U_FORTIFY_SOURCE -fno-strict-aliasing -mno-tls-direct-seg-refs"

# this is getting ridiculous, also gdb3 breaks resulting binary
#sysflags = get.CFLAGS().replace("-fstack-protector", "").replace("-D_FORTIFY_SOURCE=2", "").replace("-funwind-tables", "").replace("-fasynchronous-unwind-tables", "")
if get.ARCH() == "arm":
    sysflags = "-U_FORTIFY_SOURCE \
                -march=armv7-a -mtune=cortex-a8 -mfpu=neon -mfpu=vfp -mfloat-abi=softfp \
                -fexpensive-optimizations -fomit-frame-pointer -O2"
else:
    sysflags = "-mtune=generic -march=x86-64" if get.ARCH() == "x86_64" else "-mtune=atom -march=i686"

multibuild = (get.ARCH() == "x86_64")
pkgworkdir = "%s/%s" % (get.workDIR(), WorkDir)

config = {"multiarch": {
                "multi": True,
                "extraconfig": "--build=i686-pc-linux-gnu --enable-multi-arch",
                "coreflags":   "-m32",
                "libdir":      "lib32",
                "buildflags":  "-mtune=atom -march=i686 -O2 -pipe -fomit-frame-pointer %s" % defaultflags,
                "builddir":    "%s/build32" % pkgworkdir
            },
           "system": {
                "multi": False,
                "extraconfig": "--build=%s --host=%s" % (get.HOST(), get.HOST()),
                "coreflags":   "",
                "libdir":      "lib",
                "buildflags":  "%s %s" % (sysflags, defaultflags),
                "builddir":    "%s/build" % pkgworkdir
            }
}

ldconf32bit = """/lib32
/usr/lib32
"""
#/usr/local/lib32


### helper functions ###
def removePardusSection(_dir):
    for root, dirs, files in os.walk(_dir):
        for name in files:
            # FIXME: should we do this only on nonshared or all ?
            # if ("crt" in name and name.endswith(".o")) or name.endswith("nonshared.a"):
            if ("crt" in name and name.endswith(".o")) or name.endswith(".a"):
                i = os.path.join(root, name)
                if get.ARCH() == "arm":
                    shelltools.system('%s-objcopy -R ".comment.PARDUS.OPTs" -R ".note.gnu.build-id" %s' % (get.HOST(), i))
                else:
                    shelltools.system('objcopy -R ".comment.PARDUS.OPTs" -R ".note.gnu.build-id" %s' % i)


def set_variables(cfg):
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")

    shelltools.export("CC", "%s-gcc %s" % (get.HOST(), cfg["coreflags"]))
    shelltools.export("CXX", "%s-g++ %s" % (get.HOST(), cfg["coreflags"]))
    shelltools.export("LD", "%s-gcc" % get.HOST())

    shelltools.export("CPPFLAGS", "")
    shelltools.export("LDFLAGS", "")
    shelltools.export("CFLAGS", cfg["buildflags"])
    shelltools.export("CXXFLAGS", cfg["buildflags"])


### functionize repetetive tasks ###
def libcSetup(cfg):
    set_variables(cfg)

    if not os.path.exists(cfg["builddir"]):
        shelltools.makedirs(cfg["builddir"])

    shelltools.cd(cfg["builddir"])

    cmd = "../configure \
           --with-tls \
           --with-__thread \
           --enable-add-ons=nptl,libidn,ports \
           --enable-kernel=2.6.31 \
           --without-cvs \
           --without-selinux \
           --prefix=/usr \
           --mandir=/usr/share/man \
           --infodir=/usr/share/info \
           --libexecdir=/usr/lib/misc \
           --enable-stackguard-randomization \
           --enable-bind-now \
           --without-gd \
           --disable-profile \
           %s " % cfg["extraconfig"]

    # if arch is arm, use scratchbox for cross-build
    if get.ARCH() == "arm":
        cmd = "AUTOCONF=false sb2 %s \
               --with-abi=aapcs-linux \
               --with-headers=%s/usr/include \
               --build=%s \
               --host=%s \
               --target=%s" % (cmd, get.sysroot(), get.HOST(), get.HOST(), get.HOST())

    shelltools.system(cmd)

def libcBuild(cfg):
    set_variables(cfg)

    shelltools.cd(cfg["builddir"])

    if get.ARCH() == "arm":
        autotools.make('INSTALL=true')
    else:
        autotools.make()

def libcInstall(cfg):
    # not to bork locale/zone stuff
    set_variables(cfg)

    # install glibc/glibc-locale files
    shelltools.cd(cfg["builddir"])
    autotools.rawInstall("install_root=%s" % get.installDIR())

    # Some things want this, notably ash
    pisitools.dosym("libbsd-compat.a", "/usr/%s/libbsd.a" % cfg["libdir"])

    # Remove our options section from crt stuff
    removePardusSection("%s/usr/%s/" % (get.installDIR(), cfg["libdir"]))


### real actions start here ###
def setup():
    if not os.path.exists("ports"):
        shelltools.system("mv glibc-ports-2.12.1 ports")

    if multibuild:
        libcSetup(config["multiarch"])

    libcSetup(config["system"])


def build():
    shelltools.export("AUTOCONF", "false")
    if multibuild:
        libcBuild(config["multiarch"])

    libcBuild(config["system"])


# FIXME: yes fix me
#def check():
#    set_variables(cfg)
#    shelltools.chmod("scripts/begin-end-check.pl")
#
#    shelltools.cd("build")
#
#    shelltools.export("TIMEOUTFACTOR", "16")
#    autotools.make("-k check 2>error.log")


def install():
    # we do second arch first, to allow first arch to overwrite headers, etc.
    # stubs-32.h, elf.h, vm86.h comes only with 32bit
    if multibuild:
        libcInstall(config["multiarch"])
        pisitools.dosym("../lib32/ld-linux.so.2", "/lib/ld-linux.so.2")
        # FIXME: these should be added as additional file, when we can define pkg per arch
        pisitools.dodir("/etc/ld.so.conf.d")
        shelltools.echo("%s/etc/ld.so.conf.d/60-glibc-32bit.conf" % get.installDIR(), ldconf32bit)

    libcInstall(config["system"])

    # localedata can be shared between archs
    shelltools.cd(config["system"]["builddir"])
    autotools.rawInstall("install_root=%s localedata/install-locales" % get.installDIR())

    # now we do generic stuff
    shelltools.cd(pkgworkdir)

    # We'll take care of the cache ourselves
    if shelltools.isFile("%s/etc/ld.so.cache" % get.installDIR()):
        pisitools.remove("/etc/ld.so.cache")

    # It previously has 0755 perms which was killing things
    shelltools.chmod("%s/usr/%s/misc/pt_chown" % (get.installDIR(), config["system"]["libdir"]), 04711)

    # Prevent overwriting of the /etc/localtime symlink
    if shelltools.isFile("%s/etc/localtime" % get.installDIR()):
        pisitools.remove("/etc/localtime")

    # Nscd needs this to work
    pisitools.dodir("/var/run/nscd")
    pisitools.dodir("/var/db/nscd")

    # remove zoneinfo files since they are coming from timezone packages
    # we disable timezone build with a patch, keeping these lines for easier maintenance
    if shelltools.isDirectory("%s/usr/share/zoneinfo" % get.installDIR()):
        pisitools.removeDir("/usr/share/zoneinfo")

    for i in ["zdump", "zic"]:
        if shelltools.isFile("%s/usr/sbin/%s" % (get.installDIR(), i)):
            pisitools.remove("/usr/sbin/%s" % i)

    pisitools.dodoc("BUGS", "ChangeLog*", "CONFORMANCE", "FAQ", "NEWS", "NOTES", "PROJECTS", "README*", "LICENSES")

