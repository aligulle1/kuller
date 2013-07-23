#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dobin("dvd-slideshow")
    pisitools.dobin("dvd-menu")
    pisitools.dobin("gallery1-to-slideshow")
    pisitools.dobin("jigl2slideshow")
    pisitools.dobin("dir2slideshow")
    pisitools.doman("man/dvd-slideshow.1", "man/gallery1-to-slideshow.1", "man/dvd-menu.1", "man/dir2slideshow.1", "man/jigl2slideshow.1")
    pisitools.dodoc("COPYING.txt", "TODO.txt")
    pisitools.dohtml("doc/*.html")
