#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "speed-dreams-1.4.0-src"

def setup():
    # A whole bunch of seds just to fix the hardcoded /games/ prefix
    pisitools.dosed("src/linux/speed-dreams.in", "/games/speed-dreams", "/speed-dreams")
    pisitools.dosed("src/tools/nfsperf/sd-nfsperf.in", "/games/speed-dreams", "/speed-dreams")
    pisitools.dosed("src/tools/accc/sd-accc.in", "/games/speed-dreams", "/speed-dreams")
    pisitools.dosed("src/tools/nfs2ac/sd-nfs2ac.in", "/games/speed-dreams", "/speed-dreams")
    pisitools.dosed("src/tools/texmapper/sd-texmapper.in", "/games/speed-dreams", "/speed-dreams")
    pisitools.dosed("src/tools/trackgen/sd-trackgen.in", "/games/speed-dreams", "/speed-dreams")

    pisitools.dosed("src/tools/package/specfiles/speed-dreams-data-cars-kcendra-gt.spec.in", "/games/torcs-ng", "/torcs-ng")
    pisitools.dosed("src/tools/package/specfiles/speed-dreams-data-cars-kcendra-roadsters.spec.in", "/games/torcs-ng", "/torcs-ng")
    pisitools.dosed("src/tools/package/specfiles/speed-dreams-robot-base.spec.in", "/games/torcs-ng", "/torcs-ng")
    pisitools.dosed("src/tools/package/specfiles/speed-dreams-data-tracks-base.spec.in", "/games/torcs-ng", "/torcs-ng")
    pisitools.dosed("src/tools/package/specfiles/speed-dreams-data-cars-kcendra-sport.spec.in", "/games/torcs-ng", "/torcs-ng")
    pisitools.dosed("src/tools/package/specfiles/speed-dreams-data.spec.in", "/games/torcs-ng", "/torcs-ng")
    pisitools.dosed("src/tools/package/specfiles/speed-dreams-robot-K1999.spec.in", "/games/torcs-ng", "/torcs-ng")
    pisitools.dosed("src/tools/package/specfiles/speed-dreams-data-cars-Patwo-Design.spec.in", "/games/torcs-ng", "/torcs-ng")
    pisitools.dosed("src/tools/package/specfiles/speed-dreams-data-cars-extra.spec.in", "/games/torcs-ng", "/torcs-ng")

    pisitools.dosed("src/tools/package/specfiles/speed-dreams.spec.in", "/games/speed-dreams", "/speed-dreams")
    pisitools.dosed("data/tracks/road/ole-road-1/generate.sh", "/games/torcs", "/torcs")
    pisitools.dosed("data/tracks/road/alpine-2/alpine-2.prj.xml", "/games/torcs", "/torcs")

    autotools.configure()

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("datainstall DESTDIR=%s" % get.installDIR())
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR(), argument="datainstall")

    pisitools.insinto("/usr/share/pixmaps/", "icon.png", "speed-dreams.png")    # Desktop/pisi icon file

    pisitools.dodoc("doc/history/history.txt","COPYING","README")
    pisitools.doman("doc/man/*.6")
