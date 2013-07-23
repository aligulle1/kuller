#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():

    options = "--prefix=/usr --openssldir=/etc/pki/tls"
    otheroptions = " zlib enable-camellia enable-seed enable-tlsext enable-rfc3779 \
                     enable-cms enable-md2 threads shared -Wa,--noexecstack"

    if get.buildTYPE() == "emul32":
        options += " --libdir=lib32 --enginesdir=/usr/lib32/openssl/engines"
        shelltools.export("CFLAGS", "%s -m32" % get.CFLAGS())
        shelltools.system("./Configure linux-generic32 -m32 %s %s" % (options, otheroptions))
    else:
        options += " --libdir=lib --enginesdir=/usr/lib/openssl/engines"
        shelltools.system("./config %s %s" % (options, otheroptions))

    pisitools.dosed("Makefile", "^(SHARED_LDFLAGS=).*", "\\1 ${LDFLAGS}")
    pisitools.dosed("Makefile", "^(CFLAG=.*)", "\\1 ${CFLAGS}")

def build():
    autotools.make("depend")
    autotools.make("-j1")
    autotools.make("rehash")

#def check():
    #FIXME: Some tests write into /etc/pki directory which violates
    # sandbox rules. It is not important for now. However, we will
    # need to fix it later. (08/17/2010 --Eren)
#    homeDir = "%s/test-home" % get.workDIR()
#    shelltools.export("HOME", homeDir)
#    shelltools.makedirs(homeDir)

#    autotools.make("-j1 test")

def install():

    if get.buildTYPE() == "emul32":
        # Manually install only the needed files for emul32
        pisitools.dodir("/usr/lib32/openssl")
        pisitools.dodir("/usr/lib32/openssl/engines")
	pisitools.dodir("/usr/lib32/pkgconfig")
	#install the libraries
        pisitools.insinto("/usr/lib32","libssl.so.1.0.0")
        pisitools.insinto("/usr/lib32","libcrypto.so.1.0.0")
        #do their symlinks
        pisitools.dosym("libssl.so.1.0.0","/usr/lib32/libssl.so")
        pisitools.dosym("libcrypto.so.1.0.0","/usr/lib32/libcrypto.so")
        #install the emul32 engines
        pisitools.insinto("/usr/lib32/openssl/engines","engines/*.so")
        pisitools.insinto("/usr/lib32/openssl/engines","engines/ccgost/libgost.so")
        pisitools.insinto("/usr/lib32/pkgconfig","*.pc")

    else:
        autotools.rawInstall("INSTALL_PREFIX=%s MANDIR=/usr/share/man" % get.installDIR())
        # Move 64 bit engines to /usr/lib/openssl/engines
        pisitools.dodir("/usr/lib/openssl")
        pisitools.domove("/usr/lib/engines", "/usr/lib/openssl")

        # Certificate stuff
        pisitools.dobin("tools/c_rehash")
        pisitools.dosym("/etc/pki/tls/certs/ca-bundle.crt","/etc/pki/tls/cert.pem")

        # Rename conflicting manpages
        pisitools.rename("/usr/share/man/man1/passwd.1", "ssl-passwd.1")
        pisitools.rename("/usr/share/man/man3/rand.3", "ssl-rand.3")
        pisitools.rename("/usr/share/man/man3/err.3", "ssl-err.3")

        # Create CA dirs
        for cadir in ["CA", "CA/private", "CA/certs", "CA/crl", "CA/newcerts"]:
            pisitools.dodir("/etc/pki/%s" % cadir)

        # No static libs
        pisitools.remove("/usr/lib/*.a")

        pisitools.dohtml("doc/*")
        pisitools.dodoc("CHANGES*", "FAQ", "LICENSE", "NEWS", "README", "doc/*.txt")
