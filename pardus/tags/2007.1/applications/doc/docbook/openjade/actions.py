#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

openjade = "%s-%s-1" % (get.srcNAME(), get.srcVERSION())

def setup():
    libtools.gnuconfig_update()
    shelltools.export("ALLOWED_FLAGS", "-O -O1 -O2 -pipe -g")
    shelltools.sym("config/configure.in", "configure.in")
    shelltools.export("SGML_PREFIX", "/usr/share/sgml")
    autotools.configure("--enable-http \
                         --enable-default-catalog=/etc/sgml/catalog \
                         --enable-default-search-path=/usr/share/sgml \
                         --libdir=/usr/lib \
                         --datadir=/usr/share/sgml/%s" % openjade)

def build():
    autotools.make()

def install():
    pisitools.dodir("/usr")
    pisitools.dodir("/usr/lib")

    autotools.rawInstall("prefix=%s/usr \
                          libdir=%s/usr/lib \
                          datadir=%s/usr/share/sgml/%s "\
                          % (get.installDIR(),\
                             get.installDIR(),\
                             get.installDIR(),\
                             openjade))

    pisitools.dosym("openjade", "/usr/bin/jade")
    pisitools.dosym("onsgmls", "/usr/bin/nsgmls")
    pisitools.dosym("osgmlnorm", "/usr/bin/sgmlnorm")
    pisitools.dosym("ospam", "/usr/bin/spam")
    pisitools.dosym("ospent", "/usr/bin/spent")
    pisitools.dosym("osx", "/usr/bin/sgml2xml")

    pisitools.insinto("/usr/share/sgml/%s" % openjade, "dsssl/builtins.dsl") 

    pisitools.insinto("/usr/share/sgml/%s/dsssl" % openjade, "dsssl/dsssl.dtd") 
    pisitools.insinto("/usr/share/sgml/%s/dsssl" % openjade, "dsssl/style-sheet.dtd") 
    pisitools.insinto("/usr/share/sgml/%s/dsssl" % openjade, "dsssl/fot.dtd")
    pisitools.insinto("/usr/share/sgml/%s/pubtext" % openjade, "pubtext/*")

    pisitools.dodoc("COPYING", "NEWS", "README", "VERSION")
    pisitools.dohtml("doc/*.htm")

    pisitools.insinto("/usr/share/doc/%s-%s/jadedoc" % (openjade, get.srcRELEASE()), "jadedoc/*.htm")
    pisitools.insinto("/usr/share/doc/%s-%s/jadedoc/images" % (openjade, get.srcRELEASE()), "jadedoc/images/*")


