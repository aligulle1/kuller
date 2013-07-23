#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

docdir = "%s/%s" % (get.docDIR(), get.srcTAG())

def setup():
    shelltools.export("CFLAGS", "%s -fno-strict-aliasing" % get.CFLAGS())
    shelltools.system("./bootstrap --prefix=/usr \
                       --mandir=/usr/share/man \
                       --infodir=/usr/share/info \
                       --sysconfdir=/etc \
                       --libdir=/usr/lib \
                       --localstatedir=/var/lib \
                       --disable-warns-as-err \
                       --enable-server \
                       --datadir=/usr/share/mpeg4ip \
                       --enable-a52dec \
                       --enable-alsa \
                       --enable-arts \
                       --enable-esd \
                       --enable-faac \
                       --enable-ffmpeg=/usr/include/ffmpeg \
                       --enable-gtk-glib \
                       --enable-id3tags \
                       --enable-ipv6 \
                       --enable-mmx \
                       --enable-mp3lame \
                       --enable-mp4live \
                       --enable-mp4live-alsa \
                       --enable-mpeg2dec \
                       --enable-nas \
                       --enable-player \
                       --enable-v4l2 \
                       --enable-x264 \
                       --enable-xvid \
                       --disable-srtp \
                       --disable-ppc")

def build():
    pisitools.dosed("common/video/iso-mpeg4/src/Makefile", "-Werror")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("doc/MPEG4IP_Guide.pdf", "doc/*txt", "AUTHORS", "TODO")
    pisitools.dohtml("doc/*.html", "FEATURES.html")

    pisitools.dodir("%s/ietf" % docdir)
    pisitools.dodir("%s/mcast" % docdir)

    for f in shelltools.ls("doc/ietf/*.txt"):
        pisitools.insinto("%s/ietf/" % docdir, f)

    for f in shelltools.ls("doc/mcast/*"):
        if not "Makefile" in f:
            pisitools.insinto("%s/mcast/" % docdir, f)

    # these come from libmp4v2
    pisitools.remove("/usr/include/mp4.h")

    for f in shelltools.ls("%s/usr/lib/libmp4v2*" % get.installDIR()):
        shelltools.unlink(f)

