#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

NoStrip=["/usr/share/qemu"]

# Disabled linux-user targets: m68k, ppc, ppc64, ppc64abi32, sh4, sh4eb
user_targets=["alpha","arm","armeb","cris","i386","mips","mipsel","sparc","sparc32plus","sparc64", "x86_64"]

# Disabled softmmu targets (in addition to above) : alpha, arm, armeb
soft_targets=["cris","i386","mips","mipsel","sparc","sparc32plus","sparc64", "x86_64"]

target_list=[]

for target in user_targets:
    target_list.append("%s-linux-user" % target)

for target in soft_targets:
    target_list.append("%s-softmmu" % target)

def setup():
    autotools.rawConfigure('--prefix=/usr \
                            --enable-alsa \
                            --disable-gcc-check \
                            --target-list="%s"' % " ".join(target_list))

def build():
    autotools.make()

def install():
    autotools.rawInstall("prefix=%(INSTALL_DIR)s/usr \
                          bindir=%(INSTALL_DIR)s/usr/bin \
                          datadir=%(INSTALL_DIR)s/usr/share/qemu \
                          docdir=%(INSTALL_DIR)s/usr/share/doc/%(DOCDIR)s \
                          mandir=%(INSTALL_DIR)s/usr/share/man"
                         % {"INSTALL_DIR" : get.installDIR(), "DOCDIR" : get.srcTAG()})

    pisitools.dodoc( "Changelog", "COPYING", "README")
