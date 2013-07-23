#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")

    autotools.rawConfigure("--prefix=/usr \
                            --disable-static \
                            --disable-rpath \
                            --enable-activity-bookstore \
                            --enable-activity-configuration \
                            --enable-activity-music \
                            --enable-activity-photo \
                            --enable-activity-tv \
                            --enable-activity-video \
                            --enable-activity-weather \
                            --enable-browser-cdda \
                            --enable-browser-dvd \
                            --enable-browser-localfiles \
                            --enable-browser-valhalla \
                            --enable-browser-shoutcast \
                            --enable-browser-podcasts \
                            --enable-browser-netstreams \
                            --enable-browser-upnp \
                            --enable-input-keyboard \
                            --enable-libcurl \
                            --enable-libxml2 \
                            --enable-libxrandr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "README", "NEWS", "TODO")
