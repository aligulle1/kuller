#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "TiMidity++-%s" % get.srcVERSION()

def setup():
    audios = "flac,speex,vorbis,esd,arts,ao,nas,alsa"
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
                         --with-nas-library=/usr/lib/libaudio.so \
                         --with-default-output=alsa \
                         --enable-alsaseq' % audios)

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "doc/C/README*")
    pisitools.dosym("/etc/timidity.cfg", "/usr/share/timidity/timidity.cfg")

