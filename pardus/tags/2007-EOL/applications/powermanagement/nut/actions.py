#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "nut-2.2.1-pre1"

nutconfig = {"USER": "ups",
             "GROUP": "ups",
             "CGI_PATH": "/usr/share/nut",  # probably needs to be /var/www/localhost/cgi-bin/
             "HTML_PATH": "/usr/share/nut",  # probably needs to be /var/www/localhost/nut/
             "DRV_PATH": "/lib/nut",
             "CONF_DIR": "/etc/nut",
             "STATE_PATH": "/var/lib/nut",
             "MANDIR": "/%s" % get.manDIR(),
             "DATADIR": "/usr/share/nut"
             }


def setup():
    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.autoconf()

    pisitools.dosed("scripts/udev/Makefile.in", "52_nut-usbups.rules", "70-nut-usbups.rules")

    autotools.configure("--enable-shared \
                         --disable-static \
                         --with-user=%(USER)s \
                         --with-group=%(GROUP)s \
                         --with-drvpath=%(DRV_PATH)s \
                         --sysconfdir=%(CONF_DIR)s \
                         --with-logfacility=LOG_DAEMON \
                         --with-statepath=%(STATE_PATH)s \
                         --mandir=%(MANDIR)s \
                         --datadir=%(DATADIR)s \
                         --with-lib \
                         --with-hal \
                         --with-ssl \
                         --with-usb \
                         --with-snmp \
                         --with-cgi \
                         --with-gd-libs \
                         --with-htmlpath=%(HTML_PATH)s \
                         --with-cgipath=%(CGI_PATH)s" % nutconfig)


def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/hal/fdi/information/20thirdparty/", "scripts/hal/20-ups-nut-device.fdi")

    pisitools.dodir("/usr/libexec")
    for f in shelltools.ls("drivers"):
        if f.startswith("hald-addon-"):
            pisitools.dosym("/lib/nut/%s" % f, "/usr/libexec/%s" % f)

    # needed by scripts, this trick is for safely unmounting /usr
    pisitools.dosym("/lib/nut/upsdrvctl", "/usr/sbin/upsdrvctl")

    # nut's own statedir
    pisitools.dodir(nutconfig["STATE_PATH"])
    shelltools.chmod("%s/%s" % (get.installDIR(), nutconfig["STATE_PATH"]), 0770)

    # let configs work
    for f in shelltools.ls("%s/%s/*.sample" % (get.installDIR(), nutconfig["CONF_DIR"])):
        _file = shelltools.baseName(f)
        pisitools.rename("%s/%s" % (nutconfig["CONF_DIR"], _file), _file[:-7])

    # docs examples and cable diagrams
    pisitools.newdoc("lib/README", "README.lib")
    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcTAG()), "docs/cables")
    pisitools.dodoc("ChangeLog", "CREDITS", "MAINTAINERS", "NEWS", "README", "UPGRADING", "docs/FAQ", "docs/*.txt")

