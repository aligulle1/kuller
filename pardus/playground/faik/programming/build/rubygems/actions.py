#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import os
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

GEM_DIR = os.popen("ruby -rrbconfig -e 'puts File::expand_path(File::join(Config::CONFIG[\"sitedir\"],\"..\",\"gems\"))'").read().strip()
RUBY_VER = os.popen("ruby -rrbconfig -e 'puts Config::CONFIG[\"ruby_version\"]'").read().strip()
RUBY_SITELIB = os.popen("ruby -rrbconfig -e 'puts Config::CONFIG[\"sitelibdir\"]'").read().strip()
GEM_HOME = "%s/%s/%s" % (get.installDIR(), GEM_DIR, RUBY_VER)

def install():
    # fake home to fix sandbox violation
    shelltools.export("HOME", get.workDIR())
    shelltools.system("GEM_HOME=%s ruby setup.rb --prefix=/usr --no-rdoc --no-ri --destdir=%s/%s" % (GEM_HOME, get.installDIR(), RUBY_SITELIB))

    for i in ["rbconfig", "rubygems.rb", "rubygems", "ubygems.rb"]:
        pisitools.domove("%s/lib/%s" % (RUBY_SITELIB, i), RUBY_SITELIB)

    pisitools.removeDir("/%s/lib" % RUBY_SITELIB)
    pisitools.removeDir(GEM_DIR)

    pisitools.domove("%s/bin/gem" % RUBY_SITELIB, "/usr/bin")
    pisitools.removeDir("/%s/bin" % RUBY_SITELIB)
