#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-largefile \
                         --enable-nls \
                         --enable-install-program=arch \
                         --enable-no-install-program=faillog,hostname,login,lastlog,uptime")

def build():
    autotools.make("LDFLAGS=%s" % get.LDFLAGS())

# to be on the safe side
#def check():
#    autotools.make("check")

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move critical files into /bin
    for file in ["cat","chgrp","chmod","chown","cp","date","dd","df",
                 "dir","echo","false","ln","ls","mkdir","mknod","mv",
                 "pwd","readlink","rm","rmdir","sleep","stty","sync",
                 "touch","true","uname","vdir"]:
        pisitools.domove("/usr/bin/%s" % file, "/bin/")

    pisitools.dodoc("AUTHORS", "ChangeLog*", "NEWS", "README*", "THANKS", "TODO")
