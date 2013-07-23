#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    shelltools.cd("source/")

    autotools.configure("--with-fhs \
                         --enable-shared=yes \
                         --enable-static=no \
                         --sysconfdir=/etc/samba \
                         --localstatedir=/var \
                         --with-configdir=/etc/samba \
                         --with-libdir=/usr/lib/samba \
                         --with-piddir=/var/run/samba \
                         --with-lockdir=/var/cache/samba \
                         --with-logfilebase=/var/log/samba \
                         --with-privatedir=/var/lib/samba/private \
                         --with-pammodulesdir=/lib/security \
                         --with-libsmbclient \
                         --with-acl-support \
                         --with-ads \
                         --with-dnsupdate \
                         --with-quotas \
                         --with-sys-quotas \
                         --with-winbind \
                         --with-pam \
                         --with-pam_smbpass \
                         --with-readline \
                         --with-syslog \
                         --with-ldap \
                         --with-utmp \
                         --with-sendfile-support \
                         --with-cifsmount \
                         --with-aio-support \
                         --with-automount \
                         --without-spinlocks \
                         --without-smbmount \
                         --enable-cups \
                         --enable-swat \
                         --with-shared-modules=idmap_rid,idmap_ad")

    # Reconfigure some libraries for forcing them to generate
    # correct pkgconfig files

    shelltools.cd("lib/tdb/")
    shelltools.system("./autogen.sh")
    autotools.rawConfigure("--prefix=/usr --libdir=/usr/lib")

    shelltools.cd("../talloc/")
    shelltools.system("./autogen.sh")
    autotools.rawConfigure("--prefix=/usr --libdir=/usr/lib")

def build():
    shelltools.cd("source/")
    autotools.make("proto")
    autotools.make("everything")

def install():
    shelltools.cd("source/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-everything")

    # make install puts some libraries in the wrong place
    libs = ["smbclient", "smbsharemodes", "netapi", "talloc", "tdb", "wbclient"]
    files = [f for f in shelltools.ls("%s/usr/lib/samba" % get.installDIR()) \
             if f.startswith(tuple(["lib"+l for l in libs]))]

    for f in files:
        pisitools.domove("/usr/lib/samba/%s" % f, "/usr/lib/")

    pisitools.insinto("/usr/lib/pkgconfig", "pkgconfig/*pc")
    pisitools.insinto("/usr/lib/pkgconfig", "lib/talloc/talloc.pc")
    pisitools.insinto("/usr/lib/pkgconfig", "lib/tdb/tdb.pc")

    # we have all mount.* helpers in /usr/bin
    pisitools.domove("/usr/sbin/mount.cifs","/usr/bin/")
    pisitools.domove("/usr/sbin/umount.cifs","/usr/bin/")

    # Nsswitch extensions. Make link for wins and winbind resolvers
    pisitools.dolib_so("nsswitch/libnss_wins.so")
    pisitools.dosym("libnss_wins.so", "/usr/lib/libnss_wins.so.2")
    pisitools.dolib_so("/nsswitch/libnss_winbind.so")
    pisitools.dosym("libnss_winbind.so", "/usr/lib/libnss_winbind.so.2")

    # pam extensions
    pisitools.doexe("bin/pam_smbpass.so", "/lib/security")
    pisitools.doexe("bin/pam_winbind.so", "/lib/security")

    pisitools.dodir("/sbin")
    pisitools.dosym("/usr/bin/mount.cifs", "/sbin/mount.cifs")

    # cups support
    pisitools.dodir("/usr/lib/cups/backend")
    pisitools.dosym("/usr/bin/smbspool", "/usr/lib/cups/backend/smb")

    # directory things
    pisitools.dodir("/var/spool/samba")
    pisitools.chmod("%s/var/spool/samba" % get.installDIR(), 01777)

    pisitools.dodir("/var/log/samba")
    pisitools.dodir("/var/run/samba")
    pisitools.dodir("/var/run/winbindd")
    pisitools.dodir("/var/cache/samba")

    pisitools.dodir("/var/lib/samba/private")
    pisitools.dodir("/var/lib/samba/winbindd_privileged")
    pisitools.dodir("/var/lib/samba/netlogon")
    pisitools.dodir("/var/lib/samba/profiles")
    pisitools.dodir("/var/lib/samba/printers/W32X86")
    pisitools.dodir("/var/lib/samba/printers/WIN40")
    pisitools.dodir("/var/lib/samba/printers/W32ALPHA")
    pisitools.dodir("/var/lib/samba/printers/W32MIPS")
    pisitools.dodir("/var/lib/samba/printers/W32PPC")

    pisitools.dodir("/usr/lib/samba/auth")
    pisitools.dodir("/usr/lib/samba/idmap")

    # No swat
    pisitools.removeDir("/usr/share/samba/swat/")
