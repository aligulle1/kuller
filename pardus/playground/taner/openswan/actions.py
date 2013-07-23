#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("Makefile.inc", "(?<=INC_USRLOCAL\=).*", "/usr")
    pisitools.dosed("Makefile.inc", "(?<=INC_MANDIR\=).*", "share/man")
    pisitools.dosed("lib/libdns/Makefile", "(?<=CDEFINES \= ).*", "${USERCOMPILE} ${PORTINCLUDE}")
    pisitools.dosed("lib/libisc/Makefile", "(?<=CDEFINES \= ).*", "-DHAVE_STRERROR ${USERCOMPILE} ${PORTINCLUDE}")
    pisitools.dosed("lib/liblwres/Makefile", "(?<=CDEFINES \= ).*", "")
    pisitools.dosed("lib/liblwres/Makefile", "(?<=CWARNINGS \= ).*", "")
    pisitools.dosed("testing/utils/make-uml.sh", "WERROR=-Werror", "")
    pisitools.dosed("programs/_confread/ipsec.conf.in", "see /etc/ipsec.d", "see /usr/share/doc/openswan")

    #Pass docs
    pisitools.dosed("doc/Makefile", "(?<=programs:).*", "\npass:")
    pisitools.dosed("doc/Makefile", "(?<=install:).*", "\npass:")

def build():
    shelltools.export("FINALCONFDIR", "/etc/openswan")
    shelltools.export("FINALCONFDDIR", "/etc/openswan")
    shelltools.export("FINALCONFFILE", "/etc/openswan/ipsec.conf")
    shelltools.export("FINALLIBDIR", "/usr/lib/openswan")
    shelltools.export("FINALLIBEXECDIR", "/usr/libexec/openswan")
    shelltools.export("USE_SMARTCARD", "true")
    autotools.make("programs")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Distribution paths
    pisitools.dodir("/etc/openswan")
    pisitools.dodir("/usr/lib/openswan")
    pisitools.dodir("/usr/libexec/openswan")

    #Docs
    pisitools.domove("/etc/ipsec.d/examples", "/usr/share/doc/openswan")
    pisitools.dohtml("doc/src/*.html")
    pisitools.insinto("/usr/share/doc/openswan", "doc/quickstarts")
    pisitools.newdoc("doc/examples", "examples.txt")
    pisitools.dodoc("doc/README.x509")
    pisitools.dodoc("doc/README.XAUTH")
    pisitools.dodoc("doc/README.XAUTHclient")
    pisitools.dodoc("doc/README.NAT-Traversal")

    #Move setup script
    pisitools.remove("/usr/libexec/ipsec/setup")
    pisitools.domove("/etc/rc.d/init.d/ipsec", "/usr/libexec/openswan", "setup")

    #Collect files in right places
    pisitools.domove("/etc/ipsec.conf", "/etc/openswan")
    pisitools.domove("/etc/ipsec.d/*", "/etc/openswan")
    pisitools.domove("/usr/lib/ipsec/*", "/usr/lib/openswan")
    pisitools.domove("/usr/libexec/ipsec/*", "/usr/libexec/openswan")

    #Remove unnecessary stuff
    pisitools.removeDir("/etc/rc.d")
    pisitools.removeDir("/etc/ipsec.d")
    pisitools.removeDir("/usr/lib/ipsec")
    pisitools.removeDir("/usr/libexec/ipsec")

    #FIXME: Paths
    shelltools.system("find %s/usr/share -type f -exec sed -i 's/usr\/local/usr/' {} \;" % get.installDIR())
    shelltools.system("find %s/usr/share -type f -exec sed -i 's/etc\/ipsec.d/etc\/openswan/' {} \;" % get.installDIR())


