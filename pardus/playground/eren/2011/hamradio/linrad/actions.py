#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    # FIXME: add cases when 64-bit host is compiling the program.

    """ The make parameters are:


        To produce a Linrad executable, do one of the following:
        make linrad     - Linrad (32 bit) for Linux with svgalib.
        make linrad64   - Linrad (64 bit) for Linux with svgalib.
        make xlinrad      Linrad (32 bit) for Linux under X11
        make xlinrad64    Linrad (64 bit) for Linux under X11
        make linrad.exe - Cross compile for Windows. mingw32 needed.

        To produce scripts that install modules at boot time.
        (Reboot after sucessful completion of these commands)
        make svgalib    - For svgalib to run as a normal user.
                            svgalib_helper must be in/etc/linrad/xxxx
                            make sdr14      - To use the SDR-14 or SDR-IQ from RFSPACE

    """

    autotools.make("xlinrad")

def install():
    pisitools.dobin("xlinrad")
    pisitools.dobin("usb_sdr14")
    pisitools.dobin("svga")

    # link xlinrad to linrad
    pisitools.dosym("/usr/bin/xlinrad", "/usr/bin/linrad")

    pisitools.dodoc("*.txt")

