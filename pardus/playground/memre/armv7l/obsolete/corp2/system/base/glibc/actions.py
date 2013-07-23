#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

# FIXME: cortex-a8 specific settings!
cflags = "-U_FORTIFY_SOURCE \
          -march=armv7-a -mtune=cortex-a8 -mfpu=neon -mfpu=vfp -mfloat-abi=softfp \
          -fexpensive-optimizations -fomit-frame-pointer -O2 \
          -I%(SysRoot)s/usr/include" % crosstools.environment

def undef_variables():
    shelltools.export("LANGUAGE","C")
    shelltools.export("LANG","C")
    shelltools.export("LC_ALL","C")

    crosstools.environment["CPPFLAGS"] = ""

def setup():
    undef_variables()

    crosstools.environment["CFLAGS"] = cflags
    crosstools.prepare()

    shelltools.makedirs("build")
    shelltools.cd("build")
    shelltools.system("../configure \
                       --with-tls \
                       --build=%(build)s \
                       --host=%(host)s \
                       --target=%(target)s \
                       --with-__thread \
                       --enable-add-ons=ports,nptl,libidn \
                       --enable-bind-now \
                       --enable-kernel=2.6.25 \
                       --without-cvs \
                       --without-gd \
                       --disable-debug \
                       --without-selinux \
                       --disable-profile \
                       --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --with-headers=%(SysRoot)s/usr/include \
                       --libexecdir=/usr/lib/misc" % \
                       crosstools.environment)

def build():
    undef_variables()

    crosstools.environment["CFLAGS"] = cflags

    shelltools.cd("build")
    crosstools.make()

def install():
    undef_variables()
    installdir = get.installDIR()

    # install glibc/glibc-locale files
    shelltools.cd("build")
    crosstools.rawInstall("install_root=%s localedata/install-locales" % get.installDIR())

    # Some things want this, notably ash
    pisitools.dosym("libbsd-compat.a", "/usr/lib/libbsd.a")

    # We'll take care of the cache ourselves
    if shelltools.isFile("%s/etc/ld.so.cache" % get.installDIR()):
        pisitools.remove("/etc/ld.so.cache")

    # It previously has 0755 perms which was killing things
    shelltools.chmod("%s/usr/lib/misc/pt_chown" % get.installDIR(), 04711)

    # Prevent overwriting of the /etc/localtime symlink
    if shelltools.isFile("%s/etc/localtime" % get.installDIR()):
        pisitools.remove("/etc/localtime")

    # Nscd needs this to work
    pisitools.dodir("/var/run/nscd")
    pisitools.dodir("/var/db/nscd")

    shelltools.cd("..")

    pisitools.dodoc("BUGS", "ChangeLog*", "CONFORMANCE", "FAQ", "NEWS", "NOTES", "PROJECTS", "README*", "LICENSES")

    # remove zoneinfo files since they are coming from timezone packages
    pisitools.removeDir("/usr/share/zoneinfo")

    for i in ["zdump", "zic"]:
        pisitools.remove("/usr/sbin/%s" % i)

    # absolute-path problems with cross-compiling
    # libpthread.so, libc.so
    for lib in [ "c", "pthread" ]:
        lib = "%s/usr/lib/lib%s.so" % (installdir, lib)
        pisitools.dosed(lib, r"\s*(\/usr\/lib\/)(\S*)", " \\2" % crosstools.environment)
        pisitools.dosed(lib, r"\s*(\/lib\/\S*)", " ../..\\1" % crosstools.environment)
