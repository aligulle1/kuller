#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    shelltools.export("CXXFLAGS", get.CXXFLAGS().replace("-D_FORTIFY_SOURCE=2", ""))

    autotools.configure("--enable-smartalloc \
                         --sysconfdir=/etc/bacula \
                         --with-working-dir=/var/lib/bacula \
                         --with-scriptdir=/etc/bacula/scripts \
                         --with-plugindir=/etc/bacula/scripts \
                         --with-subsys-dir=/var/lock/subsys \
                         --with-openssl \
                         --with-python \
                         --with-mysql \
                         --disable-conio \
                         --with-db-name=bacula \
                         --with-db-user=bacula \
                         --with-tcp-wrappers \
                         --with-archivedir=/var/spool/bacula \
                         --with-hostname=localhost \
                         --with-basename=localhost \
                         --with-smtp-host=localhost \
                         --with-dir-user=bacula \
                         --with-dir-group=bacula \
                         --with-sd-user=bacula \
                         --with-sd-group=bacula \
                         --with-fd-user=root \
                         --with-fd-group=root \
                         --enable-build-stored \
                         --enable-tray-monitor \
                         --with-pid-dir=/var/run \
                         ")

    pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.chmod("%s/etc/bacula/tray-monitor.conf" % get.installDIR(), 0644)
    shelltools.chmod("%s/usr/sbin/bacula-tray-monitor" % get.installDIR(), 0755)

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "CheckList", "COPY*", \
                    "kernstodo", "LICENSE", "projects", "README*", "ReleaseNotes", \
                    "SUPPORT", "technotes", "unaccepted-projects", "VERIFYING")

    pisitools.remove("%s/%s/INSTALL" % (get.docDIR(), get.srcNAME()))


