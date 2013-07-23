#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fvi")
    shelltools.system("autopoint || touch.rpath")

    #pisitools.dosed("
    #shelltools.system("./autogen.sh \
    autotools.configure("--prefix=/usr \
                         --x-includes=%(SysRoot)s/usr/include/X11 \
                         --x-libraries=%(SysRoot)s/usr/lib \
                         --disable-static \
                         --disable-rpath \
                         --enable-glib \
                         --enable-simple-x11 \
                         --enable-ecore-config \
                         --enable-ecore-x \
                         --enable-ecore-job \
                         --enable-ecore-fb \
                         --enable-ecore-evas \
                         --enable-ecore-evas-software-16-x11 \
                         --enable-ecore-evas-xrender \
                         --enable-abstract-sockets \
                         --enable-ecore-con \
                         --enable-ecore-ipc \
                         --enable-ecore-file \
                         --enable-inotify \
                         --disable-ecore-desktop \
                         --disable-ecore-x-xcb \
                         --disable-ecore-directfb \
                         --disable-ecore-sdl \
                         --enable-ecore-evas-x11-gl \
                         --disable-ecore-evas-dfb \
                         --disable-ecore-evas-sdl \
                         --disable-openssl \
                         --disable-poll \
                         --enable-xim \
                         --disable-gnutls \
                         --with-x \
                         --with-gnu-ld \
                         --build=%(build)s \
                         --host=%(host)s" % autotools.environment )

                         #--enable-ecore-txt \
                         #--enable-ecore-evas \
                         #--enable-ecore-con \
                         #--enable-ecore-ipc \
                         #--enable-ecore-config \
                         #--enable-ecore-file \
                         #--enable-ecore-input \
                         #--enable-ecore-imf \
                         #--enable-ecore-xim \
                         #--enable-ecore-x \
                         #--enable-ecore-evas-software-buffer \
                         #--enable-ecore-evas-software-x11 \
                         #--enable-ecore-evas-xrender-x11 \
                         #--enable-ecore-evas-opengl-x11 \
                         #--enable-ecore-evas-opengl-glew \
                         #--enable-openssl \
                         #--enable-inotify \
                         #--enable-poll \
                         #--enable-curl \


def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "COPYING*", "README")
