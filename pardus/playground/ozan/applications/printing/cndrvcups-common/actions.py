#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cndrvcups-common-1.60"

def setup():
    shelltools.export("LDFLAGS", "%s -Wl,--no-as-needed" % get.LDFLAGS())

    shelltools.cd("buftool")
    shelltools.system("./autogen.sh --prefix=/%s --enable-static --disable-shared" % get.defaultprefixDIR())

    shelltools.cd("../cpca")
    shelltools.system("./autogen.sh --prefix=/%s --enable-shared --disable-static" % get.defaultprefixDIR())

    shelltools.cd("../cngplp")
    shelltools.system("./autogen.sh")

    shelltools.cd("..")

def build():
    autotools.make()

    shelltools.cd("c3plmod_ipc")
    autotools.make()
    shelltools.cd("..")

def install():
    autotools.install()

    shelltools.cd("c3plmod_ipc")
    autotools.install("DESTDIR=%s/usr/lib" % get.installDIR())
    shelltools.cd("..")

    # Manual installation of closed-source binaries
    pisitools.dobin("libs/cnpkmodule")
    pisitools.dobin("libs/c3pldrv")
    shelltools.chmod("%s/usr/bin/cnpkmodule" % get.installDIR(), mode=04755)

    # Install libraries
    pisitools.dolib_so("libs/libc3pl.so.0.0.1")
    pisitools.dolib_so("libs/libcnaccm.so.1.0")
    pisitools.dolib_so("libs/libcaepcm.so.1.0")
    pisitools.dolib_so("libs/libcaiowrap.so.1.0.0")
    pisitools.dolib_so("libs/libcaiousb.so.1.0.0")
    pisitools.dolib_so("libs/libcnlbcm.so.1.0")

    # create symlinks to libraries
    pisitools.dosym("/usr/lib/libc3pl.so.0.0.1", "/usr/lib/libc3pl.so.0")
    pisitools.dosym("/usr/lib/libc3pl.so.0.0.1", "/usr/lib/libc3pl.so")

    pisitools.dosym("/usr/lib/libcnaccm.so.1.0", "/usr/lib/libcnaccm.so.1")
    pisitools.dosym("/usr/lib/libcnaccm.so.1.0", "/usr/lib/libcnaccm.so")

    pisitools.dosym("/usr/lib/libcaepcm.so.1.0", "/usr/lib/libcaepcm.so.1")
    pisitools.dosym("/usr/lib/libcaepcm.so.1.0", "/usr/lib/libcaepcm.so")

    pisitools.dosym("/usr/lib/libcaiowrap.so.1.0.0", "/usr/lib/libcaiowrap.so.1")
    pisitools.dosym("/usr/lib/libcaiowrap.so.1.0.0", "/usr/lib/libcaiowrap.so")

    pisitools.dosym("/usr/lib/libcaiousb.so.1.0.0", "/usr/lib/libcaiousb.so.1")
    pisitools.dosym("/usr/lib/libcaiousb.so.1.0.0", "/usr/lib/libcaiousb.so")

    pisitools.dosym("/usr/lib/libcnlbcm.so.1.0", "/usr/lib/libcnlbcm.so.1")
    pisitools.dosym("/usr/lib/libcnlbcm.so.1.0", "/usr/lib/libcnlbcm.so")

    pisitools.dosym("/usr/lib/libcanonc3pl.so.1.0.0", "/usr/lib/libcanonc3pl.so")
    pisitools.dosym("/usr/lib/libcanonc3pl.so.1.0.0", "/usr/lib/libcanonc3pl.so.1")

    # Install ICC profiles
    for filename in shelltools.ls("data"):
        pisitools.insinto("/usr/share/caepcm/", "data/%s" % filename)

    # do doc's
    pisitools.dodoc("LICENSE*", "README")
