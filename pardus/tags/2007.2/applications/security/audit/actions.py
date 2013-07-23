#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get

def setup():
    autotools.autoreconf("-fv --install")
    autotools.configure("--sbindir=/sbin --with-apparmor")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=\"%s\"" % get.installDIR())
    pythonmodules.fixCompiledPy()

    # no static
    pisitools.remove("/usr/lib/*.a")
    pisitools.remove("/usr/lib/python2.4/site-packages/*.a")

    # remove RH specific bits
    pisitools.removeDir("/etc/sysconfig/")
    pisitools.removeDir("/etc/rc.d/")

    pisitools.dodir("/var/log/audit/")
