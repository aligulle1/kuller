#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install('kde4')

    # Copy Notification Rc file for Kde 4
    pisitools.insinto("%s/share/apps/package-manager/" % get.kdeDIR(), "src/package-manager.notifyrc")

    for lang in ('de','en','es','fr','nl','sv','tr'):
        pisitools.insinto("%s/share/doc/HTML/%s/package-manager/" % (get.kdeDIR(), lang),
                          "help/%s/main_help.html" % lang, "index.html")

