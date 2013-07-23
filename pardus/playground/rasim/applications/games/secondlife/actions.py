#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir="SecondLife_i686_1_20_15_92456"

def install():
    pisitools.insinto("/usr/share/SecondLife",  "*")