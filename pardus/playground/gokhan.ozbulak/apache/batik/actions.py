#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    pisitools.dodir("/usr/share/java/batik")

    pisitools.dolib("batik-rasterizer.jar", "/usr/share/java/batik")
    pisitools.dolib("batik-slideshow.jar", "/usr/share/java/batik")
    pisitools.dolib("batik-squiggle.jar", "/usr/share/java/batik")
    pisitools.dolib("batik-svgpp.jar", "/usr/share/java/batik")
    pisitools.dolib("batik-ttf2svg.jar", "/usr/share/java/batik")

    pisitools.dolib("lib/batik-anim.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-awt-util.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-bridge.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-codec.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-css.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-dom.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-extension.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-ext.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-gui-util.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-gvt.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-parser.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-script.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-svg-dom.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-svggen.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-swing.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-transcoder.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-util.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/batik-xml.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/js.jar", "/usr/share/java/batik")
    pisitools.dolib("lib/pdf-transcoder.jar", "/usr/share/java/batik")

    pisitools.dolib("extensions/batik-rasterizer-ext.jar", "/usr/share/java/batik")
    pisitools.dolib("extensions/batik-squiggle-ext.jar", "/usr/share/java/batik")

    pisitools.dohtml("docs/*")
    pisitools.dodoc("LICENSE", "NOTICE", "README", "CHANGES")
