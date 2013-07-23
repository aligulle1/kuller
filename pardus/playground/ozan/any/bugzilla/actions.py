#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010-2011 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

bzinstallprefix = "/%s" % get.dataDIR()
bzdatadir = "/%s/lib/bugzilla" % get.localstateDIR()

def setup():
    # Do some cleanup about executable bits, .CVS directories, etc.
    shelltools.system("./cleanup")

    # Remove bundled libs
    shelltools.unlink("lib/CGI*")

    # Setup cron scripts
    pisitools.dosed("cron.daily", "%%bzinstallprefix%%", bzinstallprefix)
    pisitools.dosed("cron.whine", "%%bzinstallprefix%%", bzinstallprefix)

    # Fix paths
    pisitools.dosed("contrib/*.py", "/usr/local/bin/python", "/usr/bin/python")
    pisitools.dosed("contrib/*.rb", "/usr/local/bin/ruby", "/usr/bin/ruby")
    pisitools.dosed("contrib/*.pl", "/usr/lib/sendmail", "/usr/sbin/sendmail")
    pisitools.dosed("contrib/*.pl", "/usr/local/bin/perl", "/usr/bin/perl")

def install():
    shelltools.copytree(".", "%s/%s/bugzilla" % (get.installDIR(), bzinstallprefix))

    # Duplicate English templates for Turkish ones
    # shelltools.copytree("template/en", "%s/usr/share/bugzilla/template/tr" % get.installDIR())

    # Install cron scripts into /usr/share/bugzilla
    pisitools.insinto("%s/bugzilla" % bzinstallprefix, "cron.daily")
    pisitools.insinto("%s/bugzilla" % bzinstallprefix, "cron.whine")

    pisitools.dodir(bzdatadir)
    pisitools.dodir("/etc/bugzilla")

    pisitools.dodoc("README")
