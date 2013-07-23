#!/usr/bin/python
# -*- coding: utf-8 -*-

serviceType = "server"
serviceDesc = _({"en": "Nagios Performance Data C Daemon",
                 "tr": "Nagios asenkron performans veri toplayıcı"})

from comar.service import *

NpcdRunFile="/var/run/npcd.pid"
NpcdCfgFile="/etc/pnp4nagios/npcd.cfg"
NpcdBin="/usr/sbin/npcd"

@synchronized
def start():
    startService("%s" % NpcdBin,
                 args="-d -f %s" % NpcdCfgFile,
                 pidfile="%s" % NpcdRunFile,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    stopService("%s" % NpcdRunFile,
                donotify=True)

def status():
    return isServiceRunning("%s" % NpcdRunFile)
