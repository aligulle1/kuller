#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown nagios:nagios /usr/lib/nagios/plugins/nrpe_check_control")
    os.system("/bin/chown -R root:nrpe /var/run/nrpe")
    os.system("/bin/chmod -R 775 /var/run/nrpe")
