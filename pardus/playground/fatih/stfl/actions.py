# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pass

def build():
    autotools.make("-j1 LDFLAGS=%s" % get.LDFLAGS())

def install():
    autotools.rawInstall("DESTDIR=%s \
                          prefix=/%s \
                          install"
                         %(get.installDIR(),
                           get.defaultprefixDIR()))

    # Remove unneeded files
    pisitools.remove("/usr/lib/perl5/vendor_perl/%s/%s-linux-thread-multi/example.pl"
                     % (get.curPERL(), get.ARCH()))
    pisitools.dodoc("COPYING", "README")
