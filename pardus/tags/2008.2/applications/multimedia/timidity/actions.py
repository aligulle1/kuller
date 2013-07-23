#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "TiMidity++-%s" % get.srcVERSION()

def setup():
    audios = "flac,speex,vorbis,arts,ao,alsa"

    autotools.autoconf()
    autotools.configure('--localstatedir=/var/state/timidity \
                         --with-elf \
                         --enable-audio="%s" \
                         --enable-server \
                         --enable-network \
                         --enable-dynamic \
                         --enable-vt100 \
                         --enable-spline=cubic \
                         --enable-slang \
                         --enable-ncurses \
                         --with-x \
                         --enable-spectrogram \
                         --enable-wrd \
                         --enable-xskin \
                         --enable-xaw \
                         --enable-gtk \
                         --with-default-output=alsa \
                         --enable-alsaseq' % audios)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dosym("/etc/timidity.cfg", "/usr/share/timidity/timidity.cfg")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "doc/C/README*")
