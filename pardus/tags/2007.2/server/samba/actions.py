#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    shelltools.cd("source/")

    autotools.configure("--with-fhs \
                         --sysconfdir=/etc/samba \
                         --localstatedir=/var \
                         --with-configdir=/etc/samba \
                         --with-libdir=/usr/lib/samba \
                         --with-piddir=/var/run/samba \
                         --with-lockdir=/var/cache/samba \
                         --with-logfilebase=/var/log/samba \
                         --with-privatedir=/var/lib/samba/private \
                         --with-libsmbclient \
                         --without-spinlocks \
                         --with-acl-support \
                         --with-aio-support \
                         --enable-cups \
                         --with-ldap \
                         --with-ldapsam \
                         --with-pam \
                         --with-pam_smbpass \
                         --with-python \
                         --with-quotas \
                         --with-sys-quotas \
                         --with-readline \
                         --with-smbmount \
                         --with-syslog \
                         --with-expsam=xml \
                         --with-winbind \
                         --with-shared-modules=idmap_rid")

def build():
    shelltools.cd("source/")
    autotools.make("proto")
    autotools.make("everything")

    # build python modules
    shelltools.system("python python/setup.py build")

def install():
    shelltools.cd("source/")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install-everything")

    # remove invalid symlink
    pisitools.remove("/sbin/mount.smbfs")

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
    pisitools.doexe("nsswitch/pam_winbind.so", "/lib/security")

    pisitools.dodir("/sbin")
    pisitools.dosym("/usr/bin/smbmount", "/sbin/mount.smbfs")
    pisitools.dosym("/usr/bin/mount.cifs", "/sbin/mount.cifs")

    # needed symlink
    pisitools.dosym("samba/libsmbclient.so", "/usr/lib/libsmbclient.so.0")
    pisitools.dosym("samba/libsmbclient.so", "/usr/lib/libsmbclient.so")

    # cups support
    pisitools.dodir("/usr/lib/cups/backend")
    pisitools.dosym("/usr/bin/smbspool", "/usr/lib/cups/backend/smb")

    # directory things
    pisitools.dodir("/var/spool/samba")
    pisitools.chmod("%s/var/spool/samba" % get.installDIR(), 01777)

    pisitools.dodir("/var/log/samba")
    pisitools.dodir("/var/run/samba")
    pisitools.dodir("/var/cache/samba")

    pisitools.dodir("/var/lib/samba/netlogon")
    pisitools.dodir("/var/lib/samba/profiles")
    pisitools.dodir("/var/lib/samba/printers/W32X86")
    pisitools.dodir("/var/lib/samba/printers/WIN40")
    pisitools.dodir("/var/lib/samba/printers/W32ALPHA")
    pisitools.dodir("/var/lib/samba/printers/W32MIPS")
    pisitools.dodir("/var/lib/samba/printers/W32PPC")

    pisitools.dodir("/usr/lib/samba/auth")
    pisitools.dodir("/usr/lib/samba/idmap")
    pisitools.dodir("/usr/lib/samba/auth")

    # No swat
    pisitools.removeDir("/usr/share/samba/swat/")

    # install python modules
    shelltools.system("python python/setup.py install --root=%s" % get.installDIR())
    pythonmodules.fixCompiledPy()
