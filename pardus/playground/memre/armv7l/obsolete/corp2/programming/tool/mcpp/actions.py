# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools as autotools
from pisi.actionsapi import pisitools

def setup():
    # bad fix, sorry
    for dir in [ ".", "src"]:
        pisitools.dosed("%s/Makefile.in" % dir, r"(program_transform_name|transform)\s*=.*", "\\1 =")

    autotools.configure("--enable-mcpplib --disable-static")

def build():
    autotools.make()

def install():
    autotools.install()
