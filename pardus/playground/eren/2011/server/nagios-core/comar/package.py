#!/usr/bin/python
# -*- coding: utf-8 -*-
#
import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("chown -R nagios:nagios /var/nagios/rw")
    os.system("chmod ug+s /var/nagios/rw")

    os.system("chown -R nagios:nagios /var/nagios")

    os.system("find /usr/lib/nagios -type d -print0 | xargs -0 chmod 755")
    os.system("find /usr/lib/nagios/cgi-bin -type f -print0 | xargs -0 chmod 755")
