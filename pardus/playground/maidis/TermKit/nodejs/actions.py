#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "node-v%s" % get.srcVERSION()

def setup():
    # not used shared v8 libs yet, see gentoo package:
    # http://gpo.zugaina.org/net-libs/nodejs
    shelltools.system("./configure --openssl-use-sys --shared-zlib")

def build():
    autotools.make()

def install():
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/include/node", "src/node*.h")
    pisitools.insinto("/usr/include/node", "deps/uv/include/ares*.h")
    pisitools.dobin("out/Release/node")
    pisitools.insinto("/usr/lib/node_modules/npm", "deps/npm/*")
    pisitools.dosym("/usr/lib/node_modules/npm/bin/npm-cli.js", "/usr/bin/npm")

    pisitools.dodoc("AUTHORS", "ChangeLog", "LICENSE", "README*")
