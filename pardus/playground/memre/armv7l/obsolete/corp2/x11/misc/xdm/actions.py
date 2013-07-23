# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    cache = [ "ac_cv_file__dev_urandom=yes",
              "ac_cv_file__dev_random=yes",
              "ac_cv_file_/var/log/wtmp",
              "ac_cv_file_/var/run/utmp" ]
    autotools.autoreconf("-vif")

    autotools.configure("--disable-static \
                         --enable-unix-transport \
                         --enable-tcp-transport \
                         --enable-IPv6 \
                         --enable-local-transport \
                         --enable-secure-rpc \
                         --enable-xpm-logos \
                         --enable-dynamic-greeter \
                         --enable-xdm-auth \
                         --with-pam \
                         --with-xdmconfigdir=/etc/X11/xdm \
                         --with-default-vt=vt7 \
                         --with-config-type=ws \
                         --with-xft \
                         --with-wtmp_file=/var/log/wtmp \
                         --with-utmp_file=/var/run/utmp \
                         --with-random-device=/dev/urandom \
                         --with-pixmapdir=/usr/share/X11/xdm/pixmaps", cache=cache)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/xdm")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
