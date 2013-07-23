#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

WorkDir = "OCSNG_UNIX_SERVER-1.3.2"

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import perlmodules

def build():
    shelltools.cd("Apache")
    shelltools.system("/usr/bin/perl Makefile.PL INSTALLDIRS=vendor")
    autotools.make()

def install():
    # install server
    shelltools.cd("Apache")
    autotools.make("pure_install DESTDIR=%s PREFIX=/%s" % (get.installDIR(), get.defaultprefixDIR()))
    shelltools.cd("..")
    pisitools.insinto("%s/ocsinventory-server/" % get.dataDIR(), "binutils/*")
    pisitools.remove("%s/ocsinventory-server/create-release-tarball.sh" % get.dataDIR())
    # pisitools.remove("/usr/lib/perl5/vendor_perl/5.10.1/Apache/Ocsinventory/Server/Modperl1.pm")
    pisitools.removeDir("/usr/lib/perl5/vendor_perl/5.10.1/x86_64-linux-thread-multi")
    pisitools.dodir("/var/log/ocsinventory-server")
    pisitools.dodir("%s/logrotate.d" % get.confDIR())
    pisitools.dosed("etc/logrotate.d/ocsinventory-server", "PATH_TO_LOG_DIRECTORY", "/var/log/ocsinventory-server")
    pisitools.insinto("%s/logrotate.d" % get.confDIR(), "etc/logrotate.d/ocsinventory-server")
    pisitools.insinto("%s/apache2/conf.d/" % get.confDIR(), "etc/ocsinventory/ocsinventory-server.conf", "ocsinventory-server.conf.default")
    pisitools.dosed("etc/ocsinventory/ocsinventory-server.conf", "DATABASE_SERVER", "localhost")
    pisitools.dosed("etc/ocsinventory/ocsinventory-server.conf", "DATABASE_PORT", "3306")
    pisitools.dosed("etc/ocsinventory/ocsinventory-server.conf", "VERSION_MP", "2")
    pisitools.dosed("etc/ocsinventory/ocsinventory-server.conf", "PATH_TO_LOG_DIRECTORY", "/var/log/ocsinventory-server")
    pisitools.insinto("%s/apache2/conf.d/" % get.confDIR(), "etc/ocsinventory/ocsinventory-server.conf")

    # install reports
    shelltools.copytree("%s/ocsreports" % get.curDIR(), "%s/%s/ocsinventory-reports" % ( get.installDIR(), get.dataDIR()))
    shelltools.system("/usr/bin/find %s/%s/ocsinventory-reports \( -name \*.php -o -name \*.css \) -exec chmod -x {} \;" % ( get.installDIR(), get.dataDIR()))
    pisitools.dodir("%s/ocsinventory/ocsinventory-reports" % get.confDIR())
    pisitools.domove("%s/ocsinventory-reports/dbconfig.inc.php" % get.dataDIR(), "%s/ocsinventory/ocsinventory-reports/" % get.confDIR())
    pisitools.dosym("../../../%s/ocsinventory/ocsinventory-reports/dbconfig.inc.php" % get.confDIR(), "%s/ocsinventory-reports/dbconfig.inc.php" % get.dataDIR())
    pisitools.dodir("%s/ocsinventory-reports/download" % get.localstateDIR())
    pisitools.dodir("%s/ocsinventory-reports/ipd" % get.localstateDIR())
    pisitools.insinto("%s/ocsinventory-reports/" % get.dataDIR(), "binutils/ipdiscover-util.pl")
    # pisitools.insinto("%s/apache2/vhosts.d/" % get.confDIR(), "ocsinventory-reports.conf", "ocsinventory-reports.conf.default")
    # pisitools.dosed("ocsinventory-reports.conf", "OCSREPORTS_ALIAS", "/ocsreports")
    # pisitools.dosed("ocsinventory-reports.conf", "PATH_TO_OCSREPORTS_DIR", "/%s/ocsinventory-reports" % get.dataDIR())
    # pisitools.dosed("ocsinventory-reports.conf", "PACKAGES_ALIAS", "/download")
    # pisitools.dosed("ocsinventory-reports.conf", "PATH_TO_PACKAGES_DIR", "/%s/ocsinventory-reports/download" % get.localstateDIR())
    # pisitools.insinto("%s/apache2/vhosts.d/" % get.confDIR(), "ocsinventory-reports.conf")
