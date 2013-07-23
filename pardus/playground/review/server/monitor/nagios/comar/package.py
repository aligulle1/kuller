#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R nagios:nagios /var/run/nagios")
    os.system("/bin/chown -R nagios:nagios /var/log/nagios")
    os.system("/bin/chown -R nagios:nagios /var/spool/nagios")

    os.system("/bin/chmod g+rwx /var/log/nagios/rw")
    os.system("/bin/chmod g+s /var/log/nagios/rw")
