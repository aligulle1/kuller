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

WorkDir = "openssh-%s" % get.srcVERSION().replace("_","")

def setup():
    pisitools.dosed("pathnames.h", "/usr/X11R6/bin/xauth", r"/usr/bin/xauth")
    pisitools.dosed("sshd_config", "(?m)^(^#Protocol ).*", r"Protocol 2")
    pisitools.dosed("sshd_config", "(?m)^(^#UsePAM ).*", r"UsePAM yes")
    pisitools.dosed("sshd_config", "(?m)^(^#PasswordAuthentication ).*", r"PasswordAuthentication no")
    pisitools.dosed("sshd_config", "(?m)^(^#X11Forwarding ).*", r"X11Forwarding yes")
    pisitools.dosed("sshd_config", "(?m)^(^#UseDNS ).*", r"UseDNS no")
    pisitools.dosed("sshd_config", "(?m)^(^#PermitRootLogin ).*", r"PermitRootLogin no")
    autotools.autoconf()

    autotools.configure("--sysconfdir=/etc/ssh \
                         --disable-strip \
                         --libexecdir=/usr/lib/misc \
                         --datadir=/usr/share/openssh \
                         --disable-suid-ssh  \
                         --with-privsep-path=/var/empty \
                         --with-privsep-user=sshd \
                         --with-md5-passwords \
                         --without-kerberos5 \
                         --with-tcp-wrappers \
                         --without-skey \
                         --without-opensc \
                         --with-pam")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR(), "install")

    shelltools.chmod("%s/etc/ssh/sshd_config" % get.installDIR(), 0600)
    # special request by merensan
    shelltools.echo("%s/etc/ssh/ssh_config" % get.installDIR(), "ServerAliveInterval 5")

    pisitools.dodoc("ChangeLog", "CREDITS", "OVERVIEW", "README*", "TODO", "sshd_config")
