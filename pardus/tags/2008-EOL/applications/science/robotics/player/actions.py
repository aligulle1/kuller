#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    # Highly specific drivers are disabled, reason and extra deps are in comments
    args = ( "--disable-static",
             "--disable-debug",
             "--disable-jplayer",       # java stuff is not necessary atm, build problem too
             "--with-boost-signals",
             "--with-boost-thread",
             "--disable-amtecM5",       # Amtec lib required
             #"--enable-alsa",           # Code is broken, enable when fixed
             "--disable-artoolkitplus", # Artoolkit required
             "--disable-isense",        # isense required
             "--disable-postgis",       # Postresql setup with gis plugin required
             "--disable-robotino",      # robotino lib required
             "--disable-statgrab",      # libstatgrab required
             "--disable-festival",      # FIXME: reenable when dep is in pardus
             #"--enable-sphinx2",        # FIXME: We want speech recognition
             "--disable-yarpimage",     # yarp lib required
             "--disable-phidgetRFID",   # libphidget required
             "--disable-phidgetIFK",    # ditto
             "--disable-rcore_xbridge", # libparticle required
             "--disable-sr3000",        # libusbSR required
    )
    autotools.configure(" ".join(args))

def build():
    autotools.make("-j1")

def install():
    autotools.install()
    pythonmodules.fixCompiledPy()

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "TODO")
    # Move examples under doc dir
    pisitools.domove("usr/share/player/examples", "usr/share/doc/" + get.srcTAG())
