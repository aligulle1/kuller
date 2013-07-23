#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
from comar.service import *


def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    # On first install...
    if not isServiceRunning("/var/run/mysqld/mysqld.pid"):
        startService(command="/usr/sbin/mysqld",
                     pidfile="/var/run/mysqld/mysqld.pid",
                     detach=True,donotify=True)

    # Sleep for a while
    time.sleep(3)

    # Create database and load SQL schema
    if os.system("echo 'show databases' | /usr/bin/mysql --socket=/var/run/mysqld/mysqld.sock -hlocalhost  -uroot |grep -e '^lemondb$'"):
        os.system("cat /usr/kde/4/share/apps/lemon/lemon_mysql.sql | mysql -u root")   
        
#   else:
  
#       Fixes to migrate from 0.8 to 0.9.1 database version (Yüklü paket 0.8 version ise database i yükseltmek)    ----> kontol şartı yazılacak 
#           os.system("cat /usr/kde/4/share/apps/lemon/fix_0,8.sql | mysql -u root")
#           os.system("cat /usr/kde/4/share/apps/lemon/fix_0,9.sql | mysql -u root")

#       Fixes to migrate from 0.9 to 0.9.1 database version (Yüklü paket 0.9 version ise database i yükseltmek)    ----> kontol şartı yazılacak  
#           os.system("cat /usr/kde/4/share/apps/lemon/fix_0,9.sql | mysql -u root")
