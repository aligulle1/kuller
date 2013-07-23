#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


WorkDir = "."

#ruby -rubygems -e 'puts Gem::dir' 2>/dev/null
ruby_gemdir = "/usr/lib/ruby/gems/1.8"
source = "rake-0.8.7.gem"


def install():
    shelltools.system("gem install -E --local --install-dir %s/%s  --bindir %s/usr/bin --force %s/%s" %  ( get.installDIR(), ruby_gemdir, get.installDIR(), get.workDIR(), source))

    pisitools.removeDir("%s/cache" % ruby_gemdir)

