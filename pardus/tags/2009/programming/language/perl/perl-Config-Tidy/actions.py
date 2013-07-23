#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "Config-Tiny-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.dodoc("Changes", "LICENSE", "README")
    pisitools.removeDir("/usr/lib/perl5/5.10.0")
    pisitools.removeDir("/usr/lib/perl5/vendor_perl/5.10.0/i686-linux-thread-multi/")
