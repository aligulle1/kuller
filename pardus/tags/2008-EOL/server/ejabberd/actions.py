#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# (c) TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.cd("src")
    autotools.configure()

def build():
    shelltools.cd("src")
    autotools.make("-j1")

# pdflatex fails on guide.tex
#     shelltools.cd("../doc")
#     autotools.make("html pdf")

def install():
    # ejabberdctl
    pisitools.insinto("/usr/sbin", "tools/*")

    # mnesia path
    pisitools.dodir("/var/lib/jabber/spool")

    shelltools.cd("src")
    # NOTE: Don't forget to update service.py with new versions...
    destdir = get.installDIR()
    ejabberddir = "%s/usr/lib/erlang/lib/%s-%s" % (destdir,
                                                   get.srcNAME(),
                                                   get.srcVERSION())
    etcdir = "%s/etc/jabber/" % destdir
    logdir = "%s/var/log/jabber/" % destdir
    autotools.rawInstall("DESTDIR=%s EJABBERDDIR=%s ETCDIR=%s LOGDIR=%s" % (
            destdir,
            ejabberddir,
            etcdir,
            logdir))

    pisitools.dosed("%s/etc/jabber/ejabberd.cfg" % get.installDIR(),
                    #"\.\/ssl\.pem",
                    "/path/to/ssl.pem",
                    "/etc/jabber/ssl.pem")
    shelltools.cd("../")
    pisitools.dodoc("ChangeLog", "COPYING")
