#!/usr/bin/python

import os
import os.path

def postInstall():
    os.system("/usr/bin/chown -R root:cron /var/spool/cron")
    os.system("/usr/bin/chmod -R 01730 /var/spool/cron")
    
    os.system("/usr/bin/chmod 0755 /etc/conf.d")
    
    os.system("/usr/bin/chmod 0644 /etc/pam.d/cron")
    
    os.system("/usr/bin/chown root:wheel /usr/sbin/cron")
    os.system("/usr/bin/chmod 0750 /usr/sbin/cron")
    
    os.system("/usr/bin/chown root:cron /usr/bin/crontab")
    os.system("/usr/bin/chmod 02755 /usr/bin/crontab")
    
    crontabs = "/var/spool/cron/crontabs"
    for user in os.listdir(crontabs):
        os.system("/usr/bin/chown %s:cron %s" % (user, os.path.join(crontabs, user)))
        os.system("/usr/bin/chmod 0600 %s" % os.path.join(crontabs, user))
