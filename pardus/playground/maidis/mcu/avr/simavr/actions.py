#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    pisitools.dobin("simavr/run_avr")
    pisitools.rename("/usr/bin/run_avr", "simavr")

    pisitools.dolib("simavr/obj-*-pc-linux-gnu/libsimavr.so")

    pisitools.insinto("/usr/share/simavr/tests", "tests/*")
    pisitools.insinto("/usr/share/simavr/examples", "examples/*")
    pisitools.insinto("/opt/toolchain/avr/avr/include/simavr", "include/*")

    pisitools.dodoc("COPYING", "README")
