# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

mailrc = "/%s/mail.rc" % get.confDIR()
makeflags = """
PREFIX=/%s \
BINDIR=/bin \
MANDIR=/%s \
SYSCONFDIR=/%s \
MAILRC=%s \
MAILSPOOL=/%s/mail \
SENDMAIL=/%s/sendmail \
UCBINSTALL=install""" % (get.defaultprefixDIR(), get.manDIR(), get.confDIR(), mailrc, get.localstateDIR(), get.sbinDIR())

def setup():
    pisitools.dosed("mailx.1", "/etc/nail.rc", mailrc)

def build():
    autotools.make(makeflags + " CFLAGS=\"%s -D_GNU_SOURCE\"" % get.CFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s STRIP=\"/bin/true\" %s" % (get.installDIR(), makeflags))

    pisitools.dosym("mailx", "/bin/mail")
    pisitools.dosym("mailx", "/bin/Mail")

    pisitools.dosym("mailx.1", "/%s/man1/mail.1" % get.manDIR())
    pisitools.dosym("mailx.1", "/%s/man1/Mail.1" % get.manDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
