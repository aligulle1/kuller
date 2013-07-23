#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2011 TUBITAK/BILGEM
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "gitolite-%s" % get.srcVERSION()
insDir = get.installDIR()

def install():
    shelltools.system("./src/gl-system-install %s/usr/bin \
            %s/usr/share/gitolite/conf %s/usr/share/gitolite/hooks" \
            % (insDir, insDir, insDir))
    pisitools.domove("/usr/bin/*.pm", "/usr/lib/perl5/vendor_perl/%s" \
            % get.curPERL())
    pisitools.insinto("/usr/share/gitolite/contrib/", "contrib/*")
    pisitools.insinto("/usr/share/gitolite/test/", "t/*")
    pisitools.dosed("%s/usr/bin/gl-setup"%insDir, insDir, "")
    pisitools.dosed("%s/usr/share/gitolite/conf/example.gitolite.rc"%insDir, \
            insDir, "")
