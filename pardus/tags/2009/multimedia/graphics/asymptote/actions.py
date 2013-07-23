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
    # Fixup doc dir
    pisitools.dosed("configure.ac","Datadir/doc/asymptote","Datadir/doc/asymptote-%s-%s" % (get.srcVERSION(),get.srcRELEASE()))

    autotools.autoreconf("-fi")
    autotools.configure("--enable-gc=system \
                         --with-gsl \
                         --with-latex=/usr/share/texmf-dist")

def build():
    autotools.make()

def install():
    # Use a fake $HOME environment to prevent sandbox problem
    shelltools.export("HOME",get.curDIR())

    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # add files for emacs users
    pisitools.domove("/usr/share/asymptote/*.el", "/usr/share/emacs/site-lisp/")
