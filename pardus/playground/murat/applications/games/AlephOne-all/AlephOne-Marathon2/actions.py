#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

datadir = "/usr/share/AlephOne/Marathon2"

def install():
    pisitools.insinto("%s/MML" % datadir, "MML/*")

    for data in ["Images","Map*","Shapes","Sounds","Music"]:
        pisitools.insinto(datadir, data)

    pisitools.dodoc("Marathon_2_Manual.pdf")
