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

WorkDir = "openssh-%s" % get.srcVERSION().replace("_","")

def setup():
    cache = [ "ac_cv_have_space_d_name_in_struct_dirent=${ac_cv_dirent_have_space_d_name=yes}",
              "ac_cv_have_broken_snprintf=${ac_cv_have_broken_snprintf=no}",
              "ac_cv_have_accrights_in_msghdr=${ac_cv_have_accrights_in_msghdr=no}",
              "ac_cv_have_control_in_msghdr=${ac_cv_have_control_in_msghdr=yes}",
              "ac_cv_have_openpty_ctty_bug=${ac_cv_have_openpty_ctty_bug=yes}" ]

    crosstools.environment["CFLAGS"] = "%(CFLAGS)s -fpie" % crosstools.environment
    crosstools.environment["LDFLAGS"] = "%(LDFLAGS)s -fpie" % crosstools.environment

    pisitools.dosed("pathnames.h", "/usr/X11R6/bin/xauth", r"/usr/bin/xauth")
    pisitools.dosed("sshd_config", "(?m)^(^#UsePAM ).*", r"UsePAM yes")
    pisitools.dosed("sshd_config", "(?m)^(^#PasswordAuthentication ).*", r"PasswordAuthentication no")
    pisitools.dosed("sshd_config", "(?m)^(^#X11Forwarding ).*", r"X11Forwarding yes")
    pisitools.dosed("sshd_config", "(?m)^(^#UseDNS ).*", r"UseDNS no")
    pisitools.dosed("sshd_config", "(?m)^(^#PermitRootLogin ).*", r"PermitRootLogin no")
    crosstools.autoreconf("-fi")

    pisitools.dosed("Makefile.in", r"(^AR\s*=).*", "\\1 %(AR)s" % crosstools.environment)
    pisitools.dosed("Makefile.in", r"(^LD\s*=).*", "\\1 %(CC)s" % crosstools.environment)

    crosstools.configure("--sysconfdir=/etc/ssh \
                          --disable-strip \
                          --libexecdir=/usr/lib/misc \
                          --datadir=/usr/share/openssh \
                          --with-privsep-path=/var/empty \
                          --with-privsep-user=sshd \
                          --with-md5-passwords \
                          --without-kerberos5 \
                          --with-tcp-wrappers \
                          --without-skey \
                          --without-opensc \
                          --with-pam \
                          --with-ipaddr-display \
                          --with-consolekit \
                          --without-audit", cache=cache)

def build():
    crosstools.make()

def install():
    crosstools.rawInstall("DESTDIR=%s" % get.installDIR(), "install")

    # fixes #10992
    pisitools.dobin("contrib/ssh-copy-id")
    pisitools.doman("contrib/ssh-copy-id.1")

    shelltools.chmod("%s/etc/ssh/sshd_config" % get.installDIR(), 0600)
    # special request by merensan
    shelltools.echo("%s/etc/ssh/ssh_config" % get.installDIR(), "ServerAliveInterval 5")

    pisitools.dodoc("ChangeLog", "CREDITS", "OVERVIEW", "README*", "TODO", "sshd_config")
