#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sh autogen.sh")

    autotools.configure("--libdir=/usr/lib/%s \
                         --with-mysql=/usr/bin/mysql_config \
                         --with-ldap \
                         --with-attr \
                         --with-valgrind \
                         --with-openssl \
                         --with-openssl-libs=/usr/lib \
                         --with-openssl-includes=/usr/include/openssl \
                         --with-kerberos5 \
                         --with-pcre \
                         --with-bzip2 \
                         --with-fam \
                         --with-webdav-props \
                         --with-webdav-locks \
                         --with-gdbm \
                         --with-memcache \
                         --with-lua \
                         --enable-lfs \
                         --disable-static" % get.srcNAME())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    for dirs in ["cache/lighttpd/compress", "lib/lighttpd", "log/lighttpd", "run/lighttpd"]:
        pisitools.dodir("/var/%s" % dirs)

    pisitools.dodoc("README", "ChangeLog", "COPYING", "AUTHORS", "NEWS", "doc/*.txt")
