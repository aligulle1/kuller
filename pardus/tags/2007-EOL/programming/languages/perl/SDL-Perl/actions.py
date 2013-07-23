#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="SDL_Perl-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodoc("README","CHANGELOG")

    pisitools.domove("/usr/lib/perl5/vendor_perl/5.8.8/i686-linux/auto/src/*","/usr/lib/perl5/vendor_perl/5.8.8/i686-linux/auto/")
    pisitools.removeDir("/usr/lib/perl5/vendor_perl/5.8.8/i686-linux/auto/src/")
