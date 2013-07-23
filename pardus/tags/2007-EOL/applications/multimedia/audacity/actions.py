#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "audacity-src-%s" % get.srcVERSION()

def setup():
    pisitools.dosed("configure.in", "wx-config", "wx-config-ansi")
    pisitools.dosed("configure.in", "AC_C99_FUNC_LRINT", "#AC_C99_FUNC_LRINT")
    shelltools.export("WANT_AUTOCONF", "2.5")
    autotools.autoconf()
    pisitools.dosed("configure", "^(if [^2]+) 2\.4", r"\1 2.6")
    autotools.configure("--with-libmad=system \
                         --with-vorbis=system \
                         --with-id3tag=system \
                         --with-libsndfile=system \
                         --with-libsamplerate=system \
                         --with-libflac=system \
                         --with-ladspa \
                         --with-nyquist \
                         --with-portmixer \
                         --with-soundtouch=system")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.rename("/usr/share/doc/audacity", get.srcTAG())
