#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("chown -R root:nagios /usr/lib/nagios/plugins")
    os.system("chmod -R o-rwx /usr/lib/nagios/plugins")

    os.system("chmod 04710 /usr/lib/nagios/plugins/check_icmp")
    os.system("chmod 04710 /usr/lib/nagios/plugins/check_dhcp")
