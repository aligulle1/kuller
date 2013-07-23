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

def prepare():
    shelltools.export("EX_LIBS", "-lgcc -ldl")
    shelltools.export("AS", "%(CC)s -c" % crosstools.environment)

def setup():
    crosstools.prepare()
    prepare()

    shelltools.cd("util")
    shelltools.system("perl perlpath.pl /bin")
    shelltools.cd("..")
    shelltools.system("ln -sf apps/openssl.pod crypto/crypto.pod ssl/ssl.pod doc/")

    shelltools.system("./Configure linux-elf-arm \
                       --prefix=/usr \
                       --openssldir=/etc/ssl \
                       zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
                       threads shared -Wa,--noexecstack")

    pisitools.dosed("Makefile", "(^DIRS\s*=.*)test(.*$)", "\\1 \\2" % crosstools.environment)
    pisitools.dosed("Makefile", "(^SHARED_LDFLAGS=).*", "\\1 %(LDFLAGS)s" % crosstools.environment)
    pisitools.dosed("Makefile", "(^CFLAG=.*)", "\\1 %(CFLAGS)s" % crosstools.environment)
    pisitools.dosed("apps/Makefile", r"^(LIBSSL\s*=.*)", "\\1 -L%(SysRoot)s/usr/lib -lz" % crosstools.environment)

def build():
    crosstools.make(" depend")
    crosstools.make("-j1")
    crosstools.make("rehash")

def install():
    crosstools.rawInstall("INSTALL_PREFIX=%s MANDIR=/usr/share/man" % get.installDIR())

    # Certificate stuff
    pisitools.dobin("tools/c_rehash")
    pisitools.dosym("/etc/ssl/certs/ca-bundle.crt","/etc/ssl/cert.pem")

    # Rename conflicting manpages
    pisitools.rename("/usr/share/man/man1/passwd.1", "ssl-passwd.1")
    pisitools.rename("/usr/share/man/man3/rand.3", "ssl-rand.3")
    pisitools.rename("/usr/share/man/man3/err.3", "ssl-err.3")

    # No static libs
    pisitools.remove("/usr/lib/*.a")

    pisitools.dohtml("doc/*")
    pisitools.dodoc("CHANGES*", "FAQ", "LICENSE", "NEWS", "README", "doc/*.txt")
