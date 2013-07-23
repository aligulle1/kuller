#!/usr/bin/python

import os

def postInstall():
    os.system("/usr/bin/chown tomcat:tomcat /var/tmp/tomcat5 -R")
    os.system("/usr/bin/chown tomcat:tomcat /var/run/tomcat5 -R")
    os.system("/usr/bin/chown tomcat:tomcat /var/log/tomcat5 -R")
    os.system("/usr/bin/chown tomcat:tomcat /var/lib/tomcat5 -R")
    
    os.system("/usr/bin/chmod 0755 /var/tmp/tomcat5")
    os.system("/usr/bin/chmod 0755 /var/run/tomcat5")
    os.system("/usr/bin/chmod 0755 /var/log/tomcat5")
    os.system("/usr/bin/chmod u+w  /var/lib/tomcat5 -R")
