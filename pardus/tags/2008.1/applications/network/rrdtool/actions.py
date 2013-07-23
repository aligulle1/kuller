#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-rrd-default-font=/usr/share/fonts/dejavu/DejaVuSansMono.ttf \
                         --disable-static \
                         --enable-perl \
                         --with-perl-options='installdirs=vendor destdir=%(DESTDIR)s' \
                         --enable-python \
                         --enable-ruby \
                         --with-ruby-options='sitedir=%(DESTDIR)s/usr/lib/ruby' \
                         --enable-tcl" % {"DESTDIR": get.installDIR()})

def build():
    autotools.make()

def install():
    autotools.install()

    perlmodules.fixLocalPod()

    pisitools.removeDir("/usr/share/rrdtool/fonts")
    pisitools.rename("%s/rrdtool-%s" % (get.docDIR(), get.srcVERSION()), get.srcTAG())
