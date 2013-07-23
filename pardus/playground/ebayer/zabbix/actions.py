#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#WorkDir = ""

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

commonFlags="--enable-server --enable-proxy --enable-agent \
             --with-jabber --with-net-snmp --with-ldap \
             --with-ssh2 --with-libcurl --enable-dependency-tracking"

def build():
    autotools.configure("%s --with-mysql" % commonFlags)
    autotools.make()
    shelltools.move("src/zabbix_server/zabbix_server", "%s/zabbix-1.8.3/src/zabbix_server/zabbix_server_mysql" % get.workDIR())
    shelltools.move("src/zabbix_proxy/zabbix_proxy", "%s/zabbix-1.8.3/src/zabbix_proxy/zabbix_proxy_mysql" % get.workDIR())
    autotools.configure("%s --with-pgsql" % commonFlags)
    autotools.make()
    shelltools.move("src/zabbix_server/zabbix_server", "%s/zabbix-1.8.3/src/zabbix_server/zabbix_server_pgsql" % get.workDIR())
    shelltools.move("src/zabbix_proxy/zabbix_proxy", "%s/zabbix-1.8.3/src/zabbix_proxy/zabbix_proxy_pgsql" % get.workDIR())
    autotools.configure("%s --with-sqlite3" % commonFlags)
    autotools.make()
    shelltools.move("src/zabbix_server/zabbix_server", "%s/zabbix-1.8.3/src/zabbix_server/zabbix_server_sqlite" % get.workDIR())
    shelltools.move("src/zabbix_proxy/zabbix_proxy", "%s/zabbix-1.8.3/src/zabbix_proxy/zabbix_proxy_sqlite" % get.workDIR())

def install():
    # Make some directories
    pisitools.dodir("/%s/zabbix/web" % get.confDIR())
    pisitools.dodir("/%s/zabbix" % get.dataDIR())
    pisitools.dodir("/%s/log/zabbix" % get.localstateDIR())
    pisitools.dodir("/%s/run/zabbix" % get.localstateDIR())

    # Copy web frontend
    pisitools.insinto("/%s/zabbix" % get.dataDIR(), "frontends/php/*")
    pisitools.remove("/%s/zabbix/include/.htaccess" % get.dataDIR())
    pisitools.remove("/%s/zabbix/include/classes/.htaccess" % get.dataDIR())
    pisitools.remove("/%s/zabbix/conf/zabbix.conf.php.example" % get.dataDIR())

    # Install files
    autotools.install()

    # Install binaries for all databases
    pisitools.remove("/%s/zabbix_server" % get.sbinDIR())
    pisitools.remove("/%s/zabbix_proxy" % get.sbinDIR())
    pisitools.insinto("/%s" % get.sbinDIR(), "src/zabbix_server/zabbix_server_*")
    pisitools.insinto("/%s" % get.sbinDIR(), "src/zabbix_proxy/zabbix_proxy_*")

    # Change config file variables
    pisitools.dosed("misc/conf/zabbix_agentd.conf",
                    "# PidFile=.*", "PidFile=/%s/run/zabbix/zabbix_agentd.pid" % get.localstateDIR())
    pisitools.dosed("misc/conf/zabbix_agentd.conf",
                    "^LogFile=.*", "LogFile=/%s/log/zabbix/zabbix_agentd.log" % get.localstateDIR())
    
    pisitools.dosed("misc/conf/zabbix_server.conf",
                    "# PidFile=.*", "PidFile=/%s/run/zabbix/zabbix.pid" % get.localstateDIR())
    pisitools.dosed("misc/conf/zabbix_server.conf",
                    "^LogFile=.*", "LogFile=/%s/log/zabbix/zabbix_server.log" % get.localstateDIR())
    pisitools.dosed("misc/conf/zabbix_server.conf",
                    "# AlertScriptsPath=/home/zabbix/bin/", "AlertScriptsPath=/%s/lib/zabbix/" % get.localstateDIR())
    pisitools.dosed("misc/conf/zabbix_server.conf",
                    "^DBUser=root", "DBUser=zabbix")
    pisitools.dosed("misc/conf/zabbix_server.conf",
                    "# DBSocket=/tmp/mysql.sock", "DBSocket=/%s/run/mysqld/mysqld.sock" % get.localstateDIR())

    pisitools.dosed("misc/conf/zabbix_proxy.conf",
                    "# PidFile=.*", "PidFile=/%s/run/zabbix/zabbix.pid" % get.localstateDIR())
    pisitools.dosed("misc/conf/zabbix_proxy.conf",
                    "^LogFile=.*", "LogFile=/%s/log/zabbix/zabbix_server.log" % get.localstateDIR())
    pisitools.dosed("misc/conf/zabbix_proxy.conf",
                    "^DBUser=root", "DBUser=zabbix")
    pisitools.dosed("misc/conf/zabbix_proxy.conf",
                    "# DBSocket=/tmp/mysql.sock", "DBSocket=/%s/run/mysqld/mysqld.sock" % get.localstateDIR())

    # Install config files
    pisitools.insinto("/%s/zabbix" % get.confDIR(), "misc/conf/zabbix_agent.conf")
    pisitools.insinto("/%s/zabbix" % get.confDIR(), "misc/conf/zabbix_agentd.conf")
    pisitools.insinto("/%s/zabbix" % get.confDIR(), "misc/conf/zabbix_server.conf")
    pisitools.insinto("/%s/zabbix" % get.confDIR(), "misc/conf/zabbix_proxy.conf")
    pisitools.insinto("/%s/zabbix/web" % get.confDIR(), "frontends/php/conf/zabbix.conf.php.example", destinationFile="zabbix.conf.php")

    # Install help files for databases
    pisitools.insinto("/%s/zabbix/mysql" % get.docDIR(), "create/schema/mysql.sql")
    pisitools.insinto("/%s/zabbix/mysql" % get.docDIR(), "create/data/data.sql")
    pisitools.insinto("/%s/zabbix/mysql" % get.docDIR(), "create/data/images_mysql.sql")
    pisitools.insinto("/%s/zabbix/mysql/upgrades/1.6" % get.docDIR(), "upgrades/dbpatches/1.6/mysql")
    pisitools.insinto("/%s/zabbix/mysql/upgrades/1.8" % get.docDIR(), "upgrades/dbpatches/1.8/mysql")

    pisitools.insinto("/%s/zabbix/postgresql" % get.docDIR(), "create/schema/postgresql.sql")
    pisitools.insinto("/%s/zabbix/postgresql" % get.docDIR(), "create/data/data.sql")
    pisitools.insinto("/%s/zabbix/postgresql" % get.docDIR(), "create/data/images_pgsql.sql")
    pisitools.insinto("/%s/zabbix/postgresql/upgrades/1.6" % get.docDIR(), "upgrades/dbpatches/1.6/postgresql")
    pisitools.insinto("/%s/zabbix/postgresql/upgrades/1.8" % get.docDIR(), "upgrades/dbpatches/1.8/postgresql")

    pisitools.insinto("/%s/zabbix/sqlite" % get.docDIR(), "create/schema/sqlite.sql")
    pisitools.insinto("/%s/zabbix/sqlite" % get.docDIR(), "create/data/data.sql")
    pisitools.insinto("/%s/zabbix/sqlite" % get.docDIR(), "create/data/images_sqlite3.sql")

    # Install common files
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "CREDITS", "README")
