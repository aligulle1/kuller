#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from glob import glob
from os import path

WorkDir = "."

def install():
    package_dir = applet_name = "nm-applet"
    i18n_dir = path.join(package_dir,"contents/i18n")

    # Create mo files
    for f in glob('%s/*.po' % i18n_dir):
        locale = path.basename(f).split('.')[0]
        pisitools.domo(f, locale, "%s.mo" % applet_name)
        pisitools.domove("/usr/share/locale/%s/LC_MESSAGES/%s.mo" % (locale, applet_name), "/usr/kde/4/share/locale/%s/LC_MESSAGES" % locale, "%s.mo" % applet_name)

    shelltools.unlinkDir(i18n_dir)

    pisitools.insinto("/usr/kde/4/share/apps/plasma/plasmoids", package_dir, applet_name)
    pisitools.insinto("/usr/kde/4/share/kde4/services/", "%s/metadata.desktop" % package_dir, "plasma-applet-%s.desktop" % applet_name)

    for i in range(6):
        pisitools.dosym("/usr/kde/4/share/apps/plasma/plasmoids/%s/contents/code/icons/%s.png" % (applet_name, i), "/usr/share/icons/oxygen/128x128/status/network-applet-%s.png" % i)

