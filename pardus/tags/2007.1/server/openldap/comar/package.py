#!/usr/bin/python

import os
import pwd
import grp

def postInstall():
    os.system("/usr/bin/chown ldap:ldap /var/lib/openldap-data")
    os.system("/usr/bin/chown ldap:ldap /var/lib/openldap-slurp")
    os.system("/usr/bin/chown ldap:ldap /var/run/openldap")
    os.system("/usr/bin/chown root:ldap /etc/openldap/slapd.conf")
    os.system("/usr/bin/chown root:ldap /etc/openldap/slapd.conf.default")
    os.system("/usr/bin/chmod 0700 /var/lib/openldap-data")
    os.system("/usr/bin/chmod 0700 /var/lib/openldap-slurp")
    os.system("/usr/bin/chmod 0755 /var/run/openldap")
    os.system("/usr/bin/chmod 0640 /etc/openldap/slapd.conf")
    os.system("/usr/bin/chmod 0640 /etc/openldap/slapd.conf.default")
