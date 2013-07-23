#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    # Required for scons to "see" intermediate install location
    pisitools.dodir(get.installDIR())

    # P.S: VST = 1 enables VST support which is only for personal use
    scons.make("DESTDIR='%s' \
                FPU_OPTIMIZATION=1 \
                FFT_ANALYSIS=1 \
                SYSLIBS=1 \
                LV2=0 \
                PREFIX=/usr" % (get.installDIR()))

def install():
    # Required for scons to "see" intermediate install location
    pisitools.dodir(get.installDIR())

    scons.install()
