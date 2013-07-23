#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "yoda_soccer_073"

def install():
    pisitools.dodir("/opt/yodasoccer")
    pisitools.insinto("/opt/yodasoccer", "codes")
    pisitools.insinto("/opt/yodasoccer", "data")
    pisitools.insinto("/opt/yodasoccer", "images")
    pisitools.insinto("/opt/yodasoccer", "keycodes")
    pisitools.insinto("/opt/yodasoccer", "language")
    pisitools.insinto("/opt/yodasoccer", "license")
    pisitools.insinto("/opt/yodasoccer", "music")
    pisitools.insinto("/opt/yodasoccer", "sfx")
    pisitools.insinto("/opt/yodasoccer", "yoda_soccer")
    pisitools.dosym("/opt/yodasoccer/yoda_soccer", "/usr/bin/yodasoccer")

    # Dont conflict with yodasoccer-data files
    dir = "/opt/yodasoccer/data/"

    for s in ("team_arg*", "team_mex*", "team_ofc*", "team_ecu*", "team_pol*", \
                "team_cnm*", "team_fra*", "team_ita*", "team_chi*", "team_bra*", \
                "team_col*", "team_bol*", "team_afc*", "team_per*", "team_uef*", \
                "team_par*", "team_par*", "team_tur*", "team_cyp*", "team_caf*", \
                "team_cnc*", "team_ger*", "team_arm*", "team_fin*", "team_ven*", \
                "team_uru*", "team_eng*", "team_gre*"):
        pisitools.remove(dir + s)
