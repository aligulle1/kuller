#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

shelltools.export("HOME", get.workDIR())

def setup():
    # --with-working-dir ??
    # --with-scriptdir /etc/bacula da olabilir /usr/lib/bacula da olabilir??
    # --with-plugindir scriptdirle ayni olsun.
    # --with-subsys-dir verilmeye de bilir. /var/lock/subsys emin degilim.
        # comar /var/lock/subsys altina bir .comar uzantili dosyalar olusturuyor.
    # --with-db-name vermeye illa gerek var mi?
    # --with-db-user vermeye illa gerek var mi?
    # --with-archivedir /var/spool/bacula, cunlu sonra islenecek dosyalar diye degerlendiriyoruz.
    # TODO: pathleri bir dict icinde tutup %s ile verelim, hardcoded yazmayalim actionsapi'de.
    ### --with-dir-user= root mu bacula mı? bacula diye bir user olusturana kadar root kullanalim.
    ### --with-dir-group da oldugu icin hem user hem group olusturmak elzem aslinda.
    ### TODO: dir-user, dir-group, sd-user, sd-group, fd-user, fd-group degerlerini kontrol et, simdilik
    ###       bacula diyelim hepsine.
    # enable-batch-insert enable the DB batch insert code [default=no] eklemeyi dusunebiliriz. Su an kapali
    # --with-dump-email=bacula vermemize gerek var mi acaba?
    # --enable-build-stored ???
    # --enable-lockmgr [default=no] ???

    # DEFAULT ACIK, YAZMAYA GEREK YOK.
    # --enable-ipv6
    # --enable-build-dird

    # gerekli olabilir.
    #shelltools.export("MTX", "/usr/sbin/mtx")

    # disable FORTIFY_SOURCE http://www.mail-archive.com/bacula-devel@lists.sourceforge.net/msg01786.html
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
                         --with-sd-user=bacula\
                         --with-sd-group=bacula \
                         --with-fd-user=bacula \
                         --with-fd-group=bacula \
                         --enable-build-stored \
                         --enable-tray-monitor \
                         --with-pid-dir=/var/run \
                         ")

    #pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "CheckList", "COPY*", \
                    "kernstodo", "LICENSE", "projects", "README*", "ReleaseNotes", \
                    "SUPPORT", "technotes", "unaccepted-projects", "VERIFYING")

    pisitools.remove("%s/%s/INSTALL" % (get.docDIR(), get.srcNAME()))


