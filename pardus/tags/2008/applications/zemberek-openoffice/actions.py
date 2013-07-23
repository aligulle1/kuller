#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir="."

def install():
    pisitools.insinto("/usr/share/zemberek","zemberek-ooo-1.0-Beta3-OOo_2.3.oxt","zemberek.zip")

    pisitools.echo("zemberek-release","1.02")
    pisitools.insinto("/etc","zemberek-release")
