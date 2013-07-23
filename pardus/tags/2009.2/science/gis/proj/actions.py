#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "proj-pardus-%s" % get.srcVERSION()

def setup():
    autotools.configure("--disable-static")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("%s/share/proj" % get.defaultprefixDIR(), "nad/test*")
    pisitools.insinto("%s/share/proj" % get.defaultprefixDIR(), "nad/pj_out*.dist")

    pisitools.dodoc("nad/README.NAD", "nad/README.NADUS")
