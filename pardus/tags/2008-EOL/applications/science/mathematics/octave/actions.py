#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fi")
    # All the other directories are configured through prefix.
    # autotools.configure() overrides them causing some directories
    # not prefixed by /var/pisi while installing, boom sandbox violations.
    # Briefly, use rawConfigure() here, (Fixes #8738)
    autotools.rawConfigure("--prefix=/usr \
                            --build=%s \
                            --enable-shared" % get.HOST())

def build():
    autotools.make()

def install():
    autotools.install()

    # Clean /var/pisi references
    pisitools.dosed("%s/usr/include/octave-3.0.3/octave/*" % get.installDIR(), "%s" % get.installDIR(), "")
    pisitools.dosed("%s/usr/share/octave/ls-R" % get.installDIR(), "%s" % get.installDIR(), "")
    pisitools.dosed("%s/usr/libexec/octave/ls-R" % get.installDIR(), "%s" % get.installDIR(), "")

    # Set LDPATH for octave
    pisitools.dodir("/etc/env.d")
    shelltools.echo("%s/etc/env.d/99octave" % get.installDIR(), "LDPATH=/usr/lib/octave-%s" % get.srcVERSION())
