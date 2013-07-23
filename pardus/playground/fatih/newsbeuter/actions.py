# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

opts = "DESTDIR=%s \
        prefix=/%s" % (get.installDIR(), get.defaultprefixDIR())

def build():
    autotools.make(opts)

def install():
    autotools.rawInstall("%s install" % opts)

    pisitools.dodoc("AUTHORS", "CHANGES", "LICENSE", "README", "TODO")
