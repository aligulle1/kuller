#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

ipc_types = ('sysv', 'tcp')

def setup():
    shelltools.export("LDFLAGS", "-Wl,-z,defs")

    args = '../configure \
            --prefix=/%s \
            --build=%s \
            --mandir=/%s \
            --infodir=/%s \
            --datadir=/%s \
            --sysconfdir=/%s \
            --localstatedir=/%s \
            --libexecdir=/%s \
            ' % (get.defaultprefixDIR(), \
                 get.HOST(), get.manDIR(), \
                 get.infoDIR(), get.dataDIR(), \
                 get.confDIR(), get.localstateDIR(), get.libexecDIR())

    args += "--with-pic \
             --disable-static \
             --with-ipc=%(ipc_type)s \
             --program-suffix=-%(ipc_type)s"

    for ipc_type in ipc_types:
        shelltools.makedirs(ipc_type)

        shelltools.cd(ipc_type)
        shelltools.system(args % {'ipc_type':ipc_type})
        shelltools.cd('..')

def build():
    for ipc_type in ipc_types:
        shelltools.cd(ipc_type)
        autotools.make()
        shelltools.cd('..')

def install():
    for ipc_type in ipc_types:
        shelltools.cd(ipc_type)
        autotools.install()
        shelltools.system('mv %(d)s/usr/lib/libfakeroot-{0,%(ipc)s}.so' %
                {'d'   : get.installDIR(),
                 'ipc' : ipc_type})
        shelltools.system('rm %s/usr/lib/libfakeroot.so' % get.installDIR())
        shelltools.cd('..')

    pisitools.dodoc('BUGS', 'AUTHORS', 'COPYING', 'INSTALL', 'README', 'NEWS', 'ChangeLog')

