#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

WorkDir = "smbldap-tools-0.9.5"

def setup():
    pisitools.dosed("smbldap_tools.pm", "/etc/opt/IDEALX/", "/etc/smbldap-tools/")
    pisitools.dosed("smbldap.conf", "/etc/opt/IDEALX/", "/etc/smbldap-tools/")
    pisitools.dosed("smbldap_tools.pm", "/opt/IDEALX/", "/etc/smbldap-tools/")
    pisitools.dosed("smbldap.conf", "/opt/IDEALX/", "/etc/smbldap-tools/")

def install():
    pisitools.dosbin("smbldap-*")
    pisitools.remove("/usr/sbin/smbldap-tools.spec")
    pisitools.dosbin("smbldap_tools.pm")
    pisitools.dodir("/etc/smbldap-tools")
    pisitools.insinto("/etc/smbldap-tools", "smbldap.conf")
    pisitools.insinto("/etc/smbldap-tools", "smbldap_bind.conf")
    pisitools.dodoc("CONTRIBUTORS", "COPYING", "ChangeLog", "FILES", "INFRA", \
                    "README", "TODO", "configure.pl", "*.conf")
    pisitools.dohtml("doc/html/*.html")
