#!/usr/bin/python
# -*- coding: utf-8 -*-

from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Nagios network monitor daemon",
                 "tr": "Nagios ağ izleme servisi"})

NagiosBin="/usr/bin/nagios"
NagiosCfgFile="/etc/nagios/nagios.cfg"
NagiosRunFile="/var/run/nagios/nagios.lock"

MSG_CHECK_CONFIG = _({"en" : "Check your nagios configuration. (You can check this automatically with 'nagios -v <main_config_file>' command.)",
                      "tr" : "Nagios yapılandırmasını kontrol ediniz. 'nagios -v <main_config_file>' komutu ile otomatik kontrol yapabilirsiniz."
                     })

@synchronized
def start():
    import os
    os.environ["LC_ALL"] = "C"
    os.environ["LANG"] = "C"
    try:
        startService(NagiosBin,
                    args = "-d %s" % NagiosCfgFile,
                    donotify=True)
    except:
        fail(MSG_CHECK_CONFIG)

@synchronized
def stop():
    stopService(pidfile=NagiosRunFile,
                donotify=True)

def status():
    return isServiceRunning(NagiosRunFile)
