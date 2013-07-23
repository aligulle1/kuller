#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

#ruby -rubygems -e 'puts Gem::dir' 2>/dev/null
ruby_gemdir = "/usr/lib/ruby/gems/1.8"
source = "actionpack-2.3.10.gem"

def install():
    shelltools.system("gem install -E --local --install-dir %s/%s  --bindir %s/usr/bin --force %s/%s" %  ( get.installDIR(), ruby_gemdir, get.installDIR(), get.workDIR(), source))

    pisitools.removeDir("%s/cache" % ruby_gemdir)

