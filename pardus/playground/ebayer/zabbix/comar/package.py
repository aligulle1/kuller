#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("/bin/chown -R zabbix.zabbix /var/log/zabbix")
    os.system("/bin/chown -R zabbix.zabbix /var/run/zabbix")
