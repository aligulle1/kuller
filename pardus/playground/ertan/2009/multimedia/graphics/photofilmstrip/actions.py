#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("build/photofilmstrip-cli")
    pisitools.dobin("build/photofilmstrip")
    pisitools.insinto("/usr/share/photofilmstrip", "src/*") 
    pisitools.insinto("/usr/share/applications", "build/photofilmstrip.desktop") 
    pisitools.insinto("/usr/share/pixmaps", "build/photofilmstrip.xpm")
    pisitools.domo("po/en.po", "en", "PhotoFilmStrip.mo")
    pisitools.domo("po/de.po", "de", "PhotoFilmStrip.mo")  
    pisitools.domo("po/fr.po", "fr", "PhotoFilmStrip.mo")
    pisitools.domo("po/cs.po", "cs", "PhotoFilmStrip.mo") 

    pisitools.dodoc("README", "TODO", "COPYING", "CHANGES", "doc/photofilmstrip/*")
