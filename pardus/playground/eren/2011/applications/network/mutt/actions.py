#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-gpme \
                         --enable-pop \
                         --enable-imap \
                         --enable-smtp \
                         --enable-hcache \
                         --with-regex \
                         --with-gss \
                         --with-ssl \
                         --with-sasl \
                         --with-curses \
                         --with-bdb \
                         --with-homespool=Maildir \
                         --with-mailpath=/var/spool/mail \
                         --with-docdir=/usr/share/doc/mutt")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # conflict from baselayout package
    pisitools.remove("/etc/mime.types")
