#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

from datetime import date

year, month = get.srcVERSION().split(".")
WorkDir = "hugs98-plus-%s%s" % (date(1, int(month), 1).ctime()[4:7], year)

hugsdir = "/usr/lib/hugs"

def setup():
    pisitools.dosed("packages/GLUT/GLUT.buildinfo.in", "@GLUT_LIBS@", "-lglut  -lSM -lICE -lXmu -lXi  -lGLU -lGL -lm")
    pisitools.dosed("packages/OpenGL/OpenGL.buildinfo.in", "@GLU_LIBS@", "-lGLU -lGL -lm")

    shelltools.export("hugsdir", hugsdir)
    autotools.configure("--enable-ffi \
                         --enable-profiling \
                         --enable-char-encoding=utf8 \
                         --enable-opengl \
                         --with-pthreads")

def build():
    autotools.make()

    pisitools.dosed("hugsdir/programs/hsc2hs/Paths_hsc2hs.hs", r"^(datadir *= *).*", r'\1"%s/programs/hsc2hs"' % hugsdir)

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("%s/docs/*" % hugsdir, "%s/%s" % (get.docDIR(), get.srcTAG()))
    pisitools.domove("%s/demos"  % hugsdir, "%s/%s" % (get.docDIR(), get.srcTAG()))

    pisitools.removeDir("%s/docs" % hugsdir)
    pisitools.remove("%s/Credits" % hugsdir)
    pisitools.remove("%s/License" % hugsdir)
    pisitools.remove("%s/Readme"  % hugsdir)

    pisitools.dodoc("Credits", "License", "Readme")
