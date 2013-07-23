#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir="dejavu-fonts-ttf-%s" % get.srcVERSION()
WorkDir="dejavu-fonts-ttf-2.29"

def install():
    pisitools.insinto("/usr/share/fonts/dejavu/", "ttf/*.ttf");
    pisitools.insinto("/etc/fonts/conf.avail/", "fontconfig/*.conf");

    pisitools.dosym("../conf.avail/20-unhint-small-dejavu-sans-mono.conf", "/etc/fonts/conf.d/20-unhint-small-dejavu-sans-mono.conf")
    pisitools.dosym("../conf.avail/20-unhint-small-dejavu-sans.conf", "/etc/fonts/conf.d/20-unhint-small-dejavu-sans.conf")
    pisitools.dosym("../conf.avail/20-unhint-small-dejavu-serif.conf", "/etc/fonts/conf.d/20-unhint-small-dejavu-serif.conf")
    pisitools.dosym("../conf.avail/57-dejavu-sans-mono.conf", "/etc/fonts/conf.d/57-dejavu-sans-mono.conf")
    pisitools.dosym("../conf.avail/57-dejavu-sans.conf", "/etc/fonts/conf.d/57-dejavu-sans.conf")
    pisitools.dosym("../conf.avail/57-dejavu-serif.conf", "/etc/fonts/conf.d/57-dejavu-serif.conf")

    pisitools.dodoc("AUTHORS", "LICENSE", "NEWS", "README")
