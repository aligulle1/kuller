#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

# follow upsream changes through cvs, but prefer tarball
# CVS_RSH="ssh" cvs -z3 -d:pserver:anonymous@cvs.savannah.nongnu.org:/sources/glob2 co -r alpha22-rc glob2
#
# sync data files in case upstream forgets
# rsync -rzv yog.globulation2.org::glob2data data/
# rsync -rzv yog.globulation2.org::glob2maps maps/
# rsync -rzv yog.globulation2.org::glob2campaigns campaigns/


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pisitools.dosed("configure", '^CXXFLAGS=".*', 'CXXFLAGS="%s"' % get.CXXFLAGS())
    autotools.configure("--disable-dependency-tracking \
                         --with-vorbis=/usr \
                         --with-speex=/usr \
                         --with-speex-includes=/usr/include/speex")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "README", "TODO")

    # we add our own desktop file
    pisitools.remove("/usr/share/applications/glob2.desktop")

