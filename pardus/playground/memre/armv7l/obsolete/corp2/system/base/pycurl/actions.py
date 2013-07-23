#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import crosstools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    shelltools.system("mkdir build/")
    crosstools.environment["CFLAGS"] = "%(CFLAGS)s -fPIC -I%(RootDir)s/usr/include/python2.6" % crosstools.environment
    crosstools.environment["LDFLAGS"] = "%(LDFLAGS)s -L%(RootDir)s/usr/lib/ -lpython2.6 -lcurl" % crosstools.environment

    shelltools.system("%(CC)s %(CFLAGS)s -c src/pycurl.c -o build/pycurl.o" % crosstools.environment)

    shelltools.system("%(CC)s -shared %(CFLAGS)s %(LDFLAGS)s build/pycurl.o -o build/pycurl.so" % \
                       crosstools.environment)

def install():
    shelltools.makedirs("%s/usr/lib/python2.6/site-packages/curl" % get.installDIR())

    shelltools.copy("python/curl/*py", "%s/usr/lib/python2.6/site-packages/curl/" % get.installDIR() )
    pisitools.insinto("/usr/lib/python2.6/site-packages/curl/", "build/pycurl.so")

    pisitools.dodoc("ChangeLog", "COPYING*", "README", "TODO")
