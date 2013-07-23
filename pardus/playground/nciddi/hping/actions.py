#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = 'hping2-rc3'

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    pisitools.dobin("hping2", "/usr/sbin")
    pisitools.dosym("/usr/sbin/hping2", "/usr/sbin/hping")
    pisitools.doman("docs/hping2.8")
    pisitools.dodoc("README", "AUTHORS", "CHANGES", "COPYING", "docs/AS-BACKDOOR", "docs/HPING2-IS-OPEN", "docs/MORE-FUN-WITH-IPID", "docs/*.txt")
