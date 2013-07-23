#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#WorkDir="."

def setup():
    pass

def build():
    pass

def install():

    # pardus uses sqlite3, so change the references to sqlite
    pisitools.dosed("x2gopgwrapper_sqlite", "sqlite", "sqlite3")
    pisitools.dosed("x2gosqlite.sh", "sqlite", "sqlite3")

    # we use nomachine nxagent instead of x2go version
    pisitools.dosed("x2gostartagent", "x2goagent", "nxagent")

    # install the rest in /usr/bin
    pisitools.dobin("x2go*")
    # the configuration file is written seperately, so we remote original
    pisitools.remove("/usr/bin/x2goserver.conf")
    # this is the daemon process, needs to be in /usr/sbin
    pisitools.domove("/usr/bin/x2gocleansessions", "/usr/sbin")
    # these are used once after setup, so place them in /usr/lib
    pisitools.domove("/usr/bin/x2gocreatebase.sh", "/usr/lib/x2go/script")
    pisitools.domove("/usr/bin/x2gosqlite.sh", "/usr/lib/x2go/script")
    # add some documentation
    pisitools.dodoc("INSTALL")
