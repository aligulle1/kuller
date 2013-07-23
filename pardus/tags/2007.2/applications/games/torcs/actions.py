#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    # A whole bunch of seds just to fix the hardcoded /games/ prefix
    pisitools.dosed("Make-config.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/linux/torcs.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/nfsperf/nfsperf.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/accc/accc.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/nfs2ac/nfs2ac.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/texmapper/texmapper.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-data-cars-kcendra-gt.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-data-cars-kcendra-roadsters.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/TORCS-data-cars-VM.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-robot-berniw.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-robot-base.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-data-tracks-base.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-data-cars-kcendra-sport.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-data.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-robot-K1999.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-data-cars-Patwo-Design.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs-data-cars-extra.spec.in", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/trackgen/trackgen.in", "/games/torcs", "/torcs")
    pisitools.dosed("data/tracks/road/ole-road-1/generate.sh", "/games/torcs", "/torcs")
    pisitools.dosed("src/tools/package/specfiles/torcs.spec.in", "/games/torcs", "/torcs")
    autotools.configure("--prefix=/usr --x-libraries=/usr/lib/X11")

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/share/pixmaps/", "Ticon.png", "torcs.png")
    pisitools.remove("/usr/share/torcs/COPYING")
    pisitools.dodoc("README.linux","doc/history/history.txt","COPYING","README")
    pisitools.doman("doc/man/*.6")
    autotools.rawInstall("datainstall DESTDIR=%s" % get.installDIR())
