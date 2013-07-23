#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2008  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    pisitools.dobin("test/dia")
    pisitools.dobin("test/diseqc")
    pisitools.dobin("test/sendburst")
    pisitools.dobin("test/set22k")
    pisitools.dobin("test/setpid")
    pisitools.dobin("test/setvoltage")
    pisitools.dobin("test/test_av")
    pisitools.dobin("test/test_av_play")
    pisitools.dobin("test/test_dvr")
    pisitools.dobin("test/test_dvr_play")
    pisitools.dobin("test/test_pes")
    pisitools.dobin("test/test_sec_ne")
    pisitools.dobin("test/test_sections")
    pisitools.dobin("test/test_stc")
    pisitools.dobin("test/test_stillimage")
    pisitools.dobin("test/test_tt")
    pisitools.dobin("test/test_vevent")
    pisitools.dobin("test/video")
    pisitools.dobin("util/av7110_loadkeys/av7110_loadkeys")
    pisitools.dobin("util/av7110_loadkeys/evtest")
    pisitools.dobin("util/dvbdate/dvbdate")
    pisitools.dobin("util/dvbnet/dvbnet")
    pisitools.dobin("util/dvbnet/net_start.pl")
    pisitools.dobin("util/dvbnet/net_start.sh")
    pisitools.dobin("util/dvbtraffic/dvbtraffic")
    pisitools.dobin("util/scan/scan")
    pisitools.dobin("util/szap/azap")
    pisitools.dobin("util/szap/czap")
    pisitools.dobin("util/szap/femon")
    pisitools.dobin("util/szap/szap")
    pisitools.dobin("util/szap/tzap")
    pisitools.dodoc("ChangeLog", "AUTHORS", "INSTALL*", "NEWS", "README*")