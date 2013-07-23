#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "tcp_wrappers_%s" % get.srcVERSION()

def setup():
    shelltools.chmod("Makefile", 0755)
    pisitools.dosed("Makefile", "@make", "@$(MAKE) ")
    pisitools.dosed("Makefile", "make;", "$(MAKE);")
    pisitools.dosed("Makefile", "gcc", "%(CC)s" % crosstools.environment)

def build():
    MINOR = "7"
    REL = "6"

    shelltools.export("PARDUS_CFLAGS", "%(CFLAGS)s" % crosstools.environment)

    args = 'REAL_DAEMON_DIR=%s \
            PARDUS_OPT="-fPIC -DPIC -D_REENTRANT -DHAVE_STRERROR -DHAVE_WEAKSYMS -DINET6=1 -Dss_family=__ss_family -Dss_len=__ss_len" \
            MAJOR=0 MINOR=%s REL=%s' % ( get.sbinDIR(), MINOR, REL )

    crosstools.environment["args"] = args
    crosstools.make('%(args)s config-check \
                     CC="%(CC)s" \
                     CXX="%(CXX)s" \
                     AR="%(AR)s" ' % crosstools.environment)
    crosstools.make('%(args)s LDFLAGS="-pie %(LDFLAGS)s" linux' % crosstools.environment)

def install():
    for app in ["tcpd","tcpdchk","tcpdmatch","safe_finger","try-from"]:
        pisitools.dosbin(app)

    pisitools.insinto("/usr/include", "tcpd.h")

    pisitools.dolib_a("libwrap.a")

    # FIXME: this seems not necessary anymore
    # pisitools.domove("libwrap.so", "libwrap.so.0.%s" % get.srcVERSION())
    pisitools.dolib_so("libwrap.so.0.%s" % get.srcVERSION(), "/lib")

    pisitools.dosym("libwrap.so.0.%s" % get.srcVERSION(), "/lib/libwrap.so.0")
    pisitools.dosym("libwrap.so.0", "/lib/libwrap.so")

    libtools.gen_usr_ldscript("libwrap.so")

    pisitools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.allow.5")
    pisitools.dosym("hosts_access.5", "/usr/share/man/man5/hosts.deny.5")

    pisitools.doman("*.3", "*.5", "*.8")
    pisitools.dodoc("BLURB", "CHANGES", "DISCLAIMER", "README*")

    # absolute path fix
    pisitools.dosed("%s/usr/lib/libwrap.so" % get.installDIR(),
                    r"^GROUP\s*\(.*",
                    "GROUP ( ../../lib/libwrap.so )")
