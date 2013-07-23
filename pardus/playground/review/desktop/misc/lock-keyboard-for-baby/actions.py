#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir="lk4b"

def install():
    pisitools.insinto("/usr/bin", "lock-keyboard-for-baby-20080706.pl", "lk4b")

